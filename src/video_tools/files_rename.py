"""凌乱文件重命名"""
import shutil
from pathlib import Path

from video_tools.libs.log import get_logger
from video_tools.libs.path import iter_dir_file


INPUT_DIR = Path("INPUT")
OUTPUT_DIR = Path("OUTPUT")

logger = get_logger("file_rename")

for i, src_file in enumerate(iter_dir_file(INPUT_DIR, exts=("jpg"))):
    dst_file = OUTPUT_DIR / f"XXX_{i + 1}.jpg"
    shutil.copy2(src_file, dst_file)
    logger.info(f"finished: {str(src_file)}")
    