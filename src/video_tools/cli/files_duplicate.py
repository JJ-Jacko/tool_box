"""提取指定格式的文件"""
import shutil
from typing import Dict

from video_tools import context
from video_tools.libs.datas import File
from video_tools.libs.log import get_logger
from video_tools.libs.path import get_file_hash
from video_tools.libs.path import iter_dir_file


def run():
    logger = get_logger("file_duplicate")
    existed_file_map: Dict[str, File] = dict()

    # 检查
    for src_file in iter_dir_file(context.INPUT_DIR, recurse=True, exts=("jpg")):
        hash = get_file_hash(src_file)
        
        if hash in existed_file_map:
            existed_file_map[hash].increase_times()
            logger.warning(f"duplicate file: {str(src_file)}")
            continue
        else:
            existed_file_map[hash] = File(hash, src_file)

    # 复制
    for padding_cp_file in existed_file_map.values():
        dst_file = context.OUTPUT_DIR / padding_cp_file.path.name
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
        