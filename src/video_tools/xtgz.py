"""
将src文件夹及子目录里的gz文件
批量解压
并放入dst文件夹中
"""
import os
import os.path as op

from video_tools.libs.jackolib import lsdirr_af

# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

# 遍历源文件夹中的所有gz文件
for file in lsdirr_af(SRC_DIR, 'gz'):
    # 构建源文件和目标文件的完整路径
    src_file = op.join(SRC_DIR, file)

    # 构建7z命令
    cmd = f'7z x {src_file} -o{DST_DIR}'

    # 执行命令
    os.system(cmd)
    print(f" - - -  {file} finished  - - - ")

print(f" - - -  Done!!!  - - - ")
