# MP3 Chapter Splitter

![image](https://github.com/msdousti/mp3-chapter-splitter/assets/3616518/68715220-358d-4c43-8489-f2e323e43344)


## Overview

This Python script automates the process of extracting individual chapters from an MP3 file.
It utilizes `ffprobe` to analyze the MP3 file and determine the start and end times for each chapter,
and then uses `ffmpeg` to extract and save each chapter as separate MP3 files.

## Requirements

- Python 3.x
- FFmpeg (and ffprobe) installed on your system

## Usage

1. Clone this repository or download the script `mp3_chapter_splitter.py` to your local machine.

2. Open the script in a text editor and configure the following parameters:
   - `input_file`: The path to the input MP3 file from which you want to extract chapters.
   - `output_directory`: The directory where the extracted chapters will be saved.

3. Run the script using the following command:
   ```bash
   python mp3_chapter_splitter.py
   ```


4. The script will use `ffprobe` to analyze the input MP3 file and determine the start and end times for each chapter.
   It will then use `ffmpeg` to extract and save each chapter as separate MP3 files in the specified output directory.

6. Once the script completes, you will find the individual chapters in the output directory.

## Example

Suppose you have an MP3 file named `input.mp3` with chapters, and you want to extract them into the `output_chapters/` directory. You would configure the script as follows:

```python
input_file = "input.mp3"
output_directory = "output_chapters/"
```

Then, you would run the script, and it would automatically extract all chapters and save them in the `output_chapters/` directory.

## Note
This script does not re-encode the audio during extraction, preserving the original audio quality.
