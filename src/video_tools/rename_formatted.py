"""
将src文件夹里的指定格式的文件
按指定格式排序重命名
并放入dst文件夹中
"""

from video_tools.libs.jackolib import lsdir_af
from shutil import copy
from os.path import join

# 设置输入输出文件夹
SRC_DIR="src"
DST_DIR="dst"

i = 1
# 遍历目录中的所有指定格式的文件
for file in lsdir_af(SRC_DIR, 'mp4'):
    # 重命名
    new_file = f"240716-赖俊杰-BugZapper-00{i}.mp4"

    # 构造输入输出路径
    src_file = join(SRC_DIR, file)
    dst_file = join(DST_DIR, new_file)
    
    #复制
    copy(src_file, dst_file)

    i += 1