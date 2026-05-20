import argparse

from app import download_video

def main():
    parser = argparse.ArgumentParser(description='YouTube Video Downloader')
    parser.add_argument('url', type=str, help='The URL of the YouTube video to download')
    parser.add_argument('--filetype', choices=['mp3', 'mp4'], required=True, help='Select the file type: mp3 or mp4')
    parser.add_argument('--quality', type=str, help='Specify the video quality (e.g., 720p, 1080p)')

    args = parser.parse_args()

    try:
        file_path, filename = download_video(args.url, args.filetype, args.quality)
        print(f"Downloaded: {filename} ({file_path})")
    except ValueError as exc:
        print(f"Error: {exc}")

if __name__ == '__main__':
    main()