"""duplicate all the file of spcificed extension"""

import shutil
from pathlib import Path
from typing import Dict

from tool_box.datas import File
from tool_box.log import get_logger
from tool_box.path import get_file_hash
from tool_box.path import iter_dir_file


def run(
        path_input: Path,
        path_output: Path
):
    logger = get_logger("file_duplicate", file=False)
    existed_file_map: Dict[str, File] = dict()

    # 检查
    for src_file in iter_dir_file(path_input, recurse=True, exts=("jpg")):
        hash = get_file_hash(src_file)
        
        if hash in existed_file_map:
            existed_file_map[hash].increase_times()
            logger.warning(f"duplicate file: {str(src_file)}")
            continue
        else:
            existed_file_map[hash] = File(hash, src_file)

    # 复制
    for padding_cp_file in existed_file_map.values():
        dst_file = path_output / padding_cp_file.path.name
        shutil.copy2(padding_cp_file.path, dst_file)
        logger.info(f"finished: {str(padding_cp_file.path)}")

    # 报告
    for file in existed_file_map.values():
        if file.times < 2:
            continue
        
        logger.info(
            f"File: {str(file.path)}\t"
            f"Hash: {file.hash}\t"
            f"Times: {file.times}"
        )
        