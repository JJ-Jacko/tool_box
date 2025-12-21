"""
将 src 文件夹里的 jpg 文件
反色
并放入 dst 文件夹中
"""
import os.path as op

from PIL import Image

from video_tools.libs.jackolib import lsdir_af


# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

# 遍历源文件夹中的所有 jpg 文件
for file in lsdir_af(SRC_DIR, 'jpg'):
    # 构建源文件和目标文件的完整路径
    src_file = op.join(SRC_DIR, file)
    dst_file = op.join(DST_DIR, file)

    # 打开图片文件
    image = Image.open(src_file)

    # 转换图片为RGB模式，以确保可以进行像素级操作
    image = image.convert('RGB')

    # 进行反色处理
    image = Image.eval(image, lambda p: 255 - p)

    # 保存反色处理后的图片
    image.save(dst_file)
    