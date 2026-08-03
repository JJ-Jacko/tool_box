"""反色图片"""

from PIL import Image

from video_tools import context
from video_tools.libs.log import get_logger
from video_tools.libs.path import iter_dir_file


def run():
    logger = get_logger("image_color_reverse")

    for src_file in iter_dir_file(context.INPUT_DIR, exts=context.EXTENSION.IMAGE):
        dst_file = context.OUTPUT_DIR / src_file.name
        
        image = Image.open(src_file)
        image = image.convert("RGB")
        image = Image.eval(image, lambda p: 255 - p)
        image.save(dst_file)
        
        logger.info(f"finished: {str(src_file)}")
        