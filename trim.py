from moviepy.editor import VideoFileClip

def trim_video(input_path, output_path, start_time, end_time):
    """
    Trims a video file to a specific segment.

    Args:
        input_path (str): The path to the source video file.
        output_path (str): The path to save the trimmed video file.
        start_time (float/tuple): The start time for trimming (in seconds, or (min, sec)).
        end_time (float/tuple): The end time for trimming (in seconds, or (min, sec)).
    """
    try:
        # 1. Load the video file
        clip = VideoFileClip(input_path)

        # 2. Trim the video using the subclip method
        trimmed_clip = clip.subclip(start_time, end_time)

        # 3. Write the trimmed clip to the output file
        # 'codec' specifies the video encoder (libx264 is standard for MP4)
        trimmed_clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            temp_audiofile='temp-audio.m4a', # Required for cross-platform audio handling
            remove_temp=True,
            verbose=False, 
            logger=None
        )

        print(f"✅ Video successfully trimmed and saved to: {output_path}")

    except Exception as e:
        print(f"❌ An error occurred during trimming: {e}")

# --- EXAMPLE USAGE ---

# Define file paths and times
INPUT_FILE = "videos/cam1_street.mp4"    # <-- CHANGE THIS to your video file path
OUTPUT_FILE = "cam1_street_trim.mp4" 

# Define start and end times
# You can use seconds (e.g., 10.5 for 10.5 seconds)
# Or a tuple (minutes, seconds)
START = 5.0                       # Start at 5 seconds
END = (0, 15)                     # End at 15 seconds (0 minutes, 15 seconds)

# Ensure your input file exists before running!
trim_video(INPUT_FILE, OUTPUT_FILE, START, END)