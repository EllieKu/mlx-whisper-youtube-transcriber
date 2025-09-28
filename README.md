# MLX Whisper YouTube Transcriber

A Python application that downloads YouTube videos and transcribes them to text using MLX Whisper.

## Features

- 🎥 Download audio from YouTube videos
- 🎵 Convert to MP3 format
- 📝 Transcribe audio to text with timestamps
- ⚡ Fast transcription using MLX Whisper

## Installation

1. Clone this repository
```shell
git clone <repository-url>
cd mlx-whisper-youtube-transcriber
```

2. Create virtual environment
```shell
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```shell
pip install -r requirements.txt
```

## Usage

1. Run the main script with a YouTube URL
```shell
python main.py "https://www.youtube.com/watch?v=example"
```

2. Optional: Use smaller model for faster processing
```shell
python main.py "https://www.youtube.com/watch?v=example" --small
```

3. Optional: Specify custom model
```shell
python main.py "https://www.youtube.com/watch?v=example" --model "mlx-community/whisper-large-v3-mlx"
```

4. The program will:
   - Download the video audio to `audio/` folder
   - Transcribe it using MLX Whisper
   - Save the transcript to `transcript/{channel}` folder

## Output Format

The transcript includes timestamps:
```
[0.00 - 2.50] Hello and welcome to this video
[2.50 - 5.20] Today we're going to discuss...
```
