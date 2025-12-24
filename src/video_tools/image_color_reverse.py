"""反色图片"""
from pathlib import Path

from PIL import Image

from video_tools.libs.log import get_logger
from video_tools.libs.path import iter_dir_file


INPUT_DIR = Path("INPUT")
OUTPUT_DIR = Path("OUTPUT")
IMAGE_EXTENSIONS = ("jpg", "png")

logger = get_logger("image_color_reverse")

for src_file in iter_dir_file(INPUT_DIR, exts=IMAGE_EXTENSIONS):
    dst_file = OUTPUT_DIR / src_file.name
    
    image = Image.open(src_file)
    image = image.convert("RGB")
    image = Image.eval(image, lambda p: 255 - p)
    image.save(dst_file)
    
    logger.info(f"finished: {str(src_file)}")
    