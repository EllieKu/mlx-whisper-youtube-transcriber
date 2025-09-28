import argparse
from src.downloader import download_youtube
from src.transcriber import transcribe
from src.config import WHISPER_LARGE_V3, WHISPER_SMALL


def main(url: str, model: str = WHISPER_LARGE_V3):
    """主程式：下載 YouTube 影片並轉錄為文字

    Args:
        url: YouTube 影片網址
        model: Whisper 模型名稱
    """
    (channel, title) = download_youtube(url)
    transcribe(channel, title, model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube 影片轉錄工具")
    parser.add_argument("url", help="YouTube 影片網址")
    parser.add_argument("--small", action="store_true", help="使用mlx-community/whisper-small-mlx")
    parser.add_argument("--medium", action="store_true", help="使用mlx-community/whisper-medium-mlx")
    parser.add_argument("--model", type=str, help="指定自訂模型名稱")

    args = parser.parse_args()

    if args.model:
        model = args.model
    elif args.small:
        model = WHISPER_SMALL
    else:
        model = WHISPER_LARGE_V3

    print(f"使用模型: {model}")
    main(args.url, model)