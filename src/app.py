import os
import re

import yt_dlp
from yt_dlp.utils import DownloadError


def _sanitize_filename(name):
    cleaned = re.sub(r"[^a-zA-Z0-9._ -]+", "", name).strip()
    return cleaned or "video"


def download_video(url, file_type, quality, output_dir="downloads"):
    if file_type not in {"mp3", "mp4"}:
        raise ValueError("Invalid file type selected. Please choose 'mp3' or 'mp4'.")
    if file_type == "mp4" and not quality:
        raise ValueError("Video quality is required for MP4 downloads.")

    os.makedirs(output_dir, exist_ok=True)

    height = None
    if quality:
        match = re.search(r"(\d+)", quality)
        if match:
            height = int(match.group(1))

    if file_type == "mp4":
        if height:
            format_selector = (
                f"bestvideo[ext=mp4][height={height}]+bestaudio[ext=m4a]/"
                f"best[ext=mp4][height={height}]/best[ext=mp4]"
            )
        else:
            format_selector = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
    else:
        format_selector = "bestaudio[ext=m4a]/bestaudio/best"

    ydl_opts = {
        "format": format_selector,
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "merge_output_format": "mp4",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            prepared_path = ydl.prepare_filename(info)
    except DownloadError as exc:
        raise ValueError("YouTube returned an HTTP error or blocked the request.") from exc
    except Exception as exc:
        raise ValueError("Invalid or unavailable URL.") from exc

    base_name = os.path.basename(prepared_path)
    safe_name = _sanitize_filename(base_name)
    if safe_name != base_name:
        safe_path = os.path.join(output_dir, safe_name)
        os.replace(prepared_path, safe_path)
        prepared_path = safe_path

    return prepared_path, os.path.basename(prepared_path)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    file_type = input("Select file type (mp3/mp4): ").lower()
    quality = input("Select video quality (e.g., 720p, 1080p): ")

    try:
        file_path, filename = download_video(video_url, file_type, quality)
        print(f"Downloaded: {filename} ({file_path})")
    except ValueError as exc:
        print(f"Error: {exc}")