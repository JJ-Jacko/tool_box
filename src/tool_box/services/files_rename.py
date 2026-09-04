"""rename all the file of spcificed extension"""

import shutil
from pathlib import Path
from typing import Set

from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run(
        path_input: Path,
        path_output: Path,
        extensions: Set[str]
):
    logger = get_logger("file_rename", file=False)

    for ext in extensions:
        for i, src_file in enumerate(iter_dir_file(path_input, exts={ext})):
            dst_file = path_output / f"XXX_{i + 1}.{ext}"
            shutil.copy2(src_file, dst_file)
            logger.info(f"finished: {str(src_file)}")
        