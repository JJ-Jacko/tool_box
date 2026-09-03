"""rename all the file of spcificed extension"""

import shutil
from pathlib import Path

from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run(
        path_input: Path,
        path_output: Path
):
    logger = get_logger("file_rename", file=False)

    for i, src_file in enumerate(iter_dir_file(path_input, exts=("jpg"))):
        dst_file = path_output / f"XXX_{i + 1}.jpg"
        shutil.copy2(src_file, dst_file)
        logger.info(f"finished: {str(src_file)}")
        