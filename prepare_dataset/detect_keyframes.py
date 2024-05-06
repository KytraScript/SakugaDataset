import os
import argparse
import cv2
from tqdm import tqdm
from skimage.metrics import structural_similarity

def pre_process(frame, single_channel=True):
    frame = cv2.resize(frame, (64, 64))
    if single_channel:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)[:, :, 0]
    return frame


def ssim(frame1, frame2, single_channel=True):
    if single_channel:
        return structural_similarity(pre_process(frame1, True), pre_process(frame2, True))
    return structural_similarity(pre_process(frame1, False), pre_process(frame2, False), channel_axis=-1)


def detect_keyframes(path_clip, path_kv):
    os.makedirs(os.path.dirname(path_kv), exist_ok=True)
    
    # path_clip = path_clip.replace('\\', '/')
    path_clip = "../download/split/140633/140633-Scene-001.mp4"
    print(path_clip)
    reader = cv2.VideoCapture(path_clip)
    if not reader.isOpened():
        print(f"Error: Could not open video file {path_clip}, Skipping...")
        return

    frame_width = int(reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(reader.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(path_kv, fourcc, fps, (frame_width, frame_height))

    success, prev_frame = reader.read()    # first frame must be a key frame
    if not success:
        print(f"Error: Could not read frames from {path_clip}.")
        return
    writer.write(prev_frame)
    
    while True:
        success, curr_frame = reader.read()
        if not success:
            break
        
        if ssim(prev_frame, curr_frame) < 0.95:
            writer.write(curr_frame)
        
        prev_frame = curr_frame
    
    reader.release()
    writer.release()

    return

def main(args):
    os.makedirs(args.dir_kv, exist_ok=True)
    
    for video in tqdm(os.listdir(args.dir_clip)):
        for clip in os.listdir(os.path.join(args.dir_clip, video)):
            print(clip)
            path_clip = os.path.join(args.dir_clip, video, clip)
            path_kv = os.path.join(args.dir_kv, video, clip)
            
        if not os.path.exists(os.path.basename(path_kv)) or len(os.listdir(os.path.basename(path_kv)) != len(os.path.basename(path_clip))):    # skip if already processed
            detect_keyframes(path_clip, path_kv)

if __name__ == "__main__":   
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_clip', type=str, default='../download/split', help='Root directory to the split video clips')
    parser.add_argument('--dir_kv', type=str, default='../download/kv', help='Root directory to save keyframe videos clips')
    args = parser.parse_args()
    
    main(args)
