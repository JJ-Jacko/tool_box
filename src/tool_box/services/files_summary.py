"""summary all the file"""

from typing import Dict
from pathlib import Path

from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run(path_input: Path):
    logger = get_logger("file_sum", file=False)
    existed_type_map: Dict[str, int] = dict()

    # 检查
    for src_file in iter_dir_file(path_input, recurse=True):
        suffix = src_file.suffix[1:]
        
        if suffix in existed_type_map:
            existed_type_map[suffix] += 1
        else:
            existed_type_map[suffix] = 1

    # 报告
    for ext, times in existed_type_map.items():
        logger.info(
            f"Type: {ext}\t"
            f"Times: {times}"
        )
    