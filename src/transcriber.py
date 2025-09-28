import mlx_whisper
import opencc
import os
from .utils import clean_filename

def transcribe(channel: str, filename: str, model: str):
    """轉錄音檔為文字

    Args:
        channel: 頻道名稱
        filename: 音檔檔名（不含副檔名）
        model: Whisper 模型名稱

    Returns:
        tuple: (音檔路徑, 轉錄文字檔案路徑) 或 (None, None) 如果失敗
    """
    mp3_file = f"audio/{filename}.mp3"

    try:
        clean_title = clean_filename(filename)

        if not os.path.exists(mp3_file):
            for file in os.listdir('audio'):
                if file.endswith('.mp3') and clean_title in file:
                    mp3_file = f"audio/{file}"
                    break

        print(f"開始翻譯: {filename}")

        os.makedirs(f"transcript/{channel}", exist_ok=True)
        output_txt = f"transcript/{channel}/{filename}.txt"
        outputs = mlx_whisper.transcribe(
            mp3_file,
            path_or_hf_repo=model,
            word_timestamps=True
        )
        mp3_file = f"audio/{clean_title}.mp3"

        segments = outputs["segments"]
        # ensure all output text is in Traditional Chinese
        converter = opencc.OpenCC('s2t.json')
        with open(output_txt, "w", encoding="utf-8") as file:
            for segment in segments:
                start_time = segment["start"]
                end_time = segment["end"]
                text = converter.convert(segment["text"])
                file.write(f"[{start_time:.2f} - {end_time:.2f}] {text}\n")

        print(f"轉錄完成，文字已儲存至: {output_txt}")
        return mp3_file, output_txt

    except Exception as e:
        print(f"找不到音檔: {mp3_file} - {e}")
        return None, None
