import os
import subprocess

VIDEO_FOLDER = r'D:\Other\Shotsbyhash\videouri'
THUMBNAIL_FOLDER = r'D:\Other\Shotsbyhash\videouri\thumbnails'

# Ensure output folder exists
os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)

# Time (in seconds) to grab the thumbnail frame
THUMBNAIL_TIME = 1

# Supported video file extensions
VIDEO_EXTENSIONS = ('.mp4', '.mov')

def generate_thumbnail(video_path, thumbnail_path):
    if os.path.exists(thumbnail_path):
        print(f"⚠️ Thumbnail already exists, skipping: {thumbnail_path}")
        return
    try:
        subprocess.run([
            'ffmpeg',
            '-ss', str(THUMBNAIL_TIME),
            '-i', video_path,
            '-vframes', '1',
            '-q:v', '2',
            thumbnail_path
        ], check=True, timeout=10, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Thumbnail created: {thumbnail_path}")
    except subprocess.TimeoutExpired:
        print(f"⏱️ Skipped (timeout): {video_path}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to generate thumbnail for {video_path}")

def process_videos():
    for filename in os.listdir(VIDEO_FOLDER):
        if filename.lower().endswith(VIDEO_EXTENSIONS):
            video_path = os.path.join(VIDEO_FOLDER, filename)
            base_name, _ = os.path.splitext(filename)
            thumbnail_path = os.path.join(THUMBNAIL_FOLDER, f"{base_name}.jpg")
            generate_thumbnail(video_path, thumbnail_path)

if __name__ == "__main__":
    process_videos()
