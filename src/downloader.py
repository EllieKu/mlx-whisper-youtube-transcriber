import os
import yt_dlp

def progress_hook(d):
    if d['status'] == 'finished':
        print(f"\n===下載成功===")

ydl_opts = {
    'format': 'bestaudio[ext=m4a]/bestaudio/best',
    'outtmpl': 'audio/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'progress_hooks': [progress_hook],
}

def download_youtube(url: str) -> tuple[str, str]:
    """下載 YouTube 影片音檔

    Args:
        url: YouTube 影片網址

    Returns:
        tuple: (頻道名稱, 影片標題)
    """
    os.makedirs('audio', exist_ok=True)

    print(f"===開始下載===")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        title = info.get("title", "Unknown title")
        channel = info.get("channel", "Unknown channel")

        return (channel, title)
