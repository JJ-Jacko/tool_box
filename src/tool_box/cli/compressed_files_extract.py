"""Batch extract compressed file"""

import argparse
import subprocess
from pathlib import Path

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run():
    logger = get_logger("extract", file=False)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input directory")
    parser.add_argument("-o", "--output", help="output directory")
    args = parser.parse_args()

    path_input = Path(args.input)
    if not path_input.is_dir():
        parser.error(f"{path_input} is not directory")

    if args.output:
        path_output = Path(args.output)
        if not path_output.is_dir():
            parser.error(f"{path_output} is not directory")
    else:
        path_output = Path(context.OUTPUT_DIR)

    for src_file in iter_dir_file(path_input, exts=context.EXTENSION.COMPRESSED_FILE):
        cmd = [
            "7z",
            "x", str(src_file),
            f"-o{str(path_output)}"
        ]
        subprocess.run(cmd, check=True)
        logger.info(f"finished: {str(src_file)}")


if __name__ == "__main__":
    run()