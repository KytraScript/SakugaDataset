import os
import time
import requests
import argparse
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from urllib.parse import urlparse

def download(args):
    
    os.makedirs(args.dir_download, exist_ok=True)
    
    parquets = [parquet for parquet in os.listdir(args.dir_parquets) if parquet.endswith('.parquet')]
    
    for parquet in parquets:
        
        df = pd.read_parquet(os.path.join(args.dir_parquets, parquet))
        print(f"Downloading {parquet} -->")
        
        urls = df['url_link'].tolist()
        identifiers = df['identifier'].tolist()
        
        download_dict = {}
        for url, identifier in zip(urls, identifiers):
            id_video, id_clip = identifier.split(':')
            file_extension = urlparse(url).path.split(".")[-1]
            download_dict[id_video] = {
                'url': url,
                'file_extension': file_extension
            }
        print(f"Total videos to download: {len(download_dict)}")
        
        for id_video, download_info in tqdm(download_dict.items(), total=len(download_dict), desc=f"Downloading: "):
            url = download_info['url']
            file_extension = download_info['file_extension']
            
            file_download = os.path.join(args.dir_download, f"{id_video}.{file_extension}")
            
            if os.path.exists(file_download):
                continue
            
            with open(file_download, "wb") as f:
                for chunk in requests.get(url, stream=True).iter_content(chunk_size=1024):
                    f.write(chunk)
            
            time.sleep(0.35)  # Please don't change this value
    
def main():
    cwd = Path(__file__).parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_parquets', type=str, default=str(cwd/'parquet'), help='Path to parquet files')
    parser.add_argument('--dir_download', type=str, default=str(cwd/'download'), help='Path to download the videos')
    args = parser.parse_args()
    
    download(args)

if __name__=="__main__":
    main()
