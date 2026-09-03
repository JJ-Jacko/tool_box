"""extract all the compressed files"""

import subprocess
from pathlib import Path

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run(
        path_input: Path,
        path_output: Path
):
    logger = get_logger("extract", file=False)

    for src_file in iter_dir_file(path_input, exts=context.EXTENSION.COMPRESSED_FILE):
        cmd = [
            "7z",
            "x", str(src_file),
            f"-o{str(path_output)}"
        ]
        subprocess.run(cmd, check=True)
        logger.info(f"finished: {str(src_file)}")
