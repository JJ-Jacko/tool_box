"""reverse the color of all images"""

from pathlib import Path

from PIL import Image

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run(
        path_input: Path,
        path_output: Path
):
    logger = get_logger("image_color_reverse", file=False)

    for src_file in iter_dir_file(path_input, exts=context.EXTENSION.IMAGE):
        dst_file = path_output / src_file.name
        
        image = Image.open(src_file)
        image = image.convert("RGB")
        image = Image.eval(image, lambda p: 255 - p)
        image.save(dst_file)
        
        logger.info(f"finished: {str(src_file)}")
        