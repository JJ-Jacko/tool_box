"""凌乱文件重命名"""
import shutil

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run():
    logger = get_logger("file_rename")

    for i, src_file in enumerate(iter_dir_file(context.INPUT_DIR, exts=("jpg"))):
        dst_file = context.OUTPUT_DIR / f"XXX_{i + 1}.jpg"
        shutil.copy2(src_file, dst_file)
        logger.info(f"finished: {str(src_file)}")
        