import subprocess
import re

# Define the input MP3 file and output directory
input_file = "input.mp3"
output_directory = "output_chapters/"

# Create the output directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)

# Run ffprobe to get chapter start and end times
ffprobe_cmd = f"ffprobe -show_entries chapter=start_time,end_time -of csv=p=0 -v error {input_file}"
ffprobe_output = subprocess.check_output(ffprobe_cmd, shell=True, text=True)

# Parse the ffprobe output to extract chapter start and end times
chapter_times = re.findall(r"([\d:.]+),([\d:.]+)", ffprobe_output)

# Extract each chapter using ffmpeg
for i, (start_time, end_time) in enumerate(chapter_times, start=1):
    output_file = f"{output_directory}chapter_{i}.mp3"
    ffmpeg_cmd = (
        f"ffmpeg -i {input_file} -ss {start_time} -to {end_time} -c copy {output_file}"
    )
    subprocess.call(ffmpeg_cmd, shell=True)

print("Extraction of chapters completed.")
