"""重新编码媒体"""
import subprocess
from pathlib import Path

from video_tools.libs.log import get_logger
from video_tools.libs.path import iter_dir_file


INPUT_DIR = Path("INPUT")
OUTPUT_DIR = Path("OUTPUT")
MEDIA_EXTENSIONS = ("mp4", "mov", "flv", "avi")

logger = get_logger("encoding_media")

for src_file in iter_dir_file(INPUT_DIR, exts=MEDIA_EXTENSIONS):
    dst_file = OUTPUT_DIR / f"{src_file.stem}.mp4"
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-i", str(src_file),
        "-c:v", "libx264",
        str(dst_file)
    ]
    subprocess.run(cmd, check=True)
    logger.info(f"finished: {str(src_file)}")
    