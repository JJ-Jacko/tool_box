"""
将src文件夹里的指定格式的文件
复制指定数量
按指定格式排序重命名
并放入dst文件夹中
"""

from video_tools.libs.jackolib import lsdir_af
from os.path import join
from shutil import copy

# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

# 设置复制数量
num = 8

# 遍历源文件夹中的所有指定格式的文件
for file in lsdir_af(SRC_DIR, 'png'): #设置源文件格式
    src_file = join(SRC_DIR, file)
    for i in range(1, num + 1):
        format = f'{file}_{i}.png' #设置复制格式
        dst_file = join(DST_DIR, format)
        copy(src_file, dst_file)