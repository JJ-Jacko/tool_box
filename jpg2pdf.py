"""
将 src 文件夹里的 jpg 图片
按顺序合并到一个 pdf 文件
并放入 dst 文件夹中
"""

from re import findall
from os import system
from os.path import join
from jackolib import lsdir_af

def sort_key(item):
    """
    为 sort 函数构造 sort_key
    规则：按照字符串后面的数字排序
    """
    number = findall(r'\d+', item)
    if number:
        return int(number[0])
    else:
        return 0

# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

# 初始化 magick 命令
cmd = f'magick '

# 遍历源文件夹中的所有 jpg 文件
files = lsdir_af(SRC_DIR, 'jpg')
files.sort(key=sort_key)
for file in files:
    # 构建源文件的完整路径
    src_file = join(SRC_DIR, file)
    # 添加到 magick 命令中
    cmd += f'"{src_file}" '

# 构建目标文件的完整路径
dst_file = join(DST_DIR, 'output.pdf')

# 构建完整 magick 命令
cmd += f'"{dst_file}"'

# 执行命令
system(cmd)
print(f" - - -  Done!!!  - - - ")