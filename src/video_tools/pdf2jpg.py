"""
将 src 文件夹里的多页 pdf 文件
拆分成多个 jpg 图片
并放入 dst 文件夹中
"""
import os
import os.path as op

from video_tools.libs.jackolib import lsdir_af

# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

# 遍历源文件夹中的所有 mp4 文件
for file in lsdir_af(SRC_DIR, 'pdf'):
    # 构建源文件和目标文件的完整路径
    src_file = op.join(SRC_DIR, file)
    dst_file = op.join(DST_DIR, op.splitext(file)[0])

    # 构建 pdftocairo 命令
    cmd = f'pdftocairo -jpeg {src_file} {dst_file}'

    # 执行命令
    os.system(cmd)
    print(f" - - -  {file} finished  - - - ")

print(f" - - -  Done!!!  - - - ")
