import os
import argparse
import pandas as pd
from scenedetect import split_video_ffmpeg, FrameTimecode
from scenedetect import detect, AdaptiveDetector
from collections import defaultdict
from tqdm import tqdm


def fetch_boudaries(df):
    df['identifier_video'] = df['identifier'].apply(lambda x: int(x.split(':')[0]))
    df['identifier_clip'] = df['identifier'].apply(lambda x: int(x.split(':')[1]))
    df = df.sort_values(by=['identifier_video', 'identifier_clip'])
    
    boudaries = defaultdict(list)
    for i in range(len(df)):
        row = df.iloc[i]
        identifier_video = row['identifier_video']
        identifier_clip = row['identifier_clip']
        start_time = row['scene_start_time']
        end_time = row['scene_end_time']
        fps = row['fps']
        
        boudaries[identifier_video].append((FrameTimecode(start_time, fps), FrameTimecode(end_time, fps)))
    
    return boudaries


def split_video_from_parquet(args):   
    for path_parquet in os.listdir(args.dir_parquet):
        print(f'Processing {path_parquet}')
        
        df = pd.read_parquet(os.path.join(args.dir_parquet, path_parquet))
        df = df[['identifier', 'scene_start_time', 'scene_end_time', 'fps']]
        
        # drop rows with nan
        df = df.dropna(subset=['scene_start_time', 'scene_end_time', 'fps'])
        
        # fetch the boundaries from the parquet file
        boudaries = fetch_boudaries(df)
        
        # split the videos using the boundaries
        for video in tqdm(os.listdir(args.dir_video), desc='Splitting videos'):
            if video.endswith('.gitkeep'):
                continue
            
            vid_identifier = os.path.splitext(video)[0]
            
            if int(vid_identifier) not in list(boudaries.keys()): # current parquet file doesn't has the boundaries for the video
                continue
                
            path_video = os.path.join(args.dir_video, video)
            dir_save = os.path.join(args.dir_out, vid_identifier)   # split clips will be saved to a new directory named as video
            os.makedirs(dir_save, exist_ok=True)
            
            boundary = boudaries[int(vid_identifier)]
            
            if len(os.listdir(dir_save)) != len(boundary):  # if the video is already split, skip
                split_video_ffmpeg(path_video, boundary, output_file_template=f'{dir_save}/$VIDEO_NAME-Scene-$SCENE_NUMBER.mp4')

def split_video_from_detection(path_video, dir_save):
    '''
    In case the scene information is not provided in parquet files(i.e. NaN, new videos),
    you can use this fast api to split the videos using the PySceneDetect.
    '''
    boundary = detect(path_video, AdaptiveDetector(adaptive_threshold=3.0, min_scene_len=18, min_content_val=30.0))
    
    split_video_ffmpeg(path_video, boundary, output_file_template=f'{dir_save}/$VIDEO_NAME-Scene-$SCENE_NUMBER.mp4')
    
    # remember to save the boundary information for future usage
    

if __name__=="__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_parquet', type=str, default=r'../download/parquet', help='Directory to the parquet files')
    parser.add_argument('--dir_video', type=str, default=r'../download/download', help='Directory to the downloaded videos')
    parser.add_argument('--dir_out', type=str, default=r'../download/split', help='Directory to save the split videos')
    args = parser.parse_args()
    
    split_video_from_parquet(args)