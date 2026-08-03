"""批量解压文件"""
import subprocess

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run():
    logger = get_logger("extract")

    for src_file in iter_dir_file(context.INPUT_DIR, exts=context.EXTENSION.COMPRESSED_FILE):
        cmd = [
            "7z",
            "x", str(src_file),
            f"-o{str(context.OUTPUT_DIR)}"
        ]
        subprocess.run(cmd, check=True)
        logger.info(f"finished: {str(src_file)}")
    