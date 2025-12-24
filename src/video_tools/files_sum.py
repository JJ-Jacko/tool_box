"""统计文件"""
from pathlib import Path
from typing import Dict

from video_tools.libs.log import get_logger
from video_tools.libs.path import iter_dir_file


INPUT_DIR = Path("INPUT")

logger = get_logger("file_sum")
existed_type_map: Dict[str, int] = dict()

# 检查
for src_file in iter_dir_file(INPUT_DIR, recurse=True):
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
    