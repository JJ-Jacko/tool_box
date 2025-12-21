"""
将src文件夹里的mp4文件
以h264格式
重新编码
"""

from video_tools.libs.jackolib import lsdir_af
from os import system
from os.path import join

# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

# 遍历源文件夹中的所有mp4文件
for file in lsdir_af(SRC_DIR, 'mp4'):
    # 构建源文件和目标文件的完整路径
    src_file = join(SRC_DIR, file)
    dst_file = join(DST_DIR, file)

    # 构建ffmpeg命令
    cmd = f'ffmpeg -hide_banner -i "{src_file}" -c:v libx264 "{dst_file}"'

    # 执行命令
    system(cmd)
    print(f" - - -  {file} finished  - - - ")

print(f" - - -  Done!!!  - - - ")
