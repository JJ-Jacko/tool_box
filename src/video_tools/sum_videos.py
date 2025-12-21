"""统计共有src目录下共有多少mp4文件"""

from video_tools.libs.jackolib import lsdirr_af

# 设置源文件夹
SRC_DIR='src'

files = lsdirr_af(SRC_DIR, 'mp4')

for file in files:
    print(file)
print(len(files))