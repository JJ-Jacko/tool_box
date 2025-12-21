"""
将src文件夹及子文件夹的指定格式的文件
去重复
按排序重命名
并放入dst文件夹中
并报告重复文件的次数和对应哈希值
"""

from video_tools.libs.jackolib import lsdirr_af, calc_file_hash
from os.path import join
from shutil import copy

# 设置源文件夹和目标文件夹
SRC_DIR='src'
DST_DIR='dst'

files = [] #存储将复制的文件
hashs = []
duplicate_files = [] #存储重复文件对象
class Duplicate_file:
    """模拟重复的文件"""
    def __init__(self, name, hash):
        self.name = name
        self.hash = hash
        self.times = 1
    
    def increase_times(self):
        """递增重复次数"""
        self.times += 1

# 检查
for file in lsdirr_af(SRC_DIR, 'mp4'):
    src_file = join(SRC_DIR, file)
    hash = calc_file_hash(src_file)
    if hash in hashs:
        """
        发现重复文件
        更新重复对象列表
        以备报告
        """
        if duplicate_files:
            """之后的添加修改"""
            for f in duplicate_files:
                """
                发现hash重复
                此文件对象存在
                递增出现次数
                """
                if hash == f.hash:
                    f.increase_times()
                    break
            else:
                """
                未发现hash重复
                此文件对象不存在
                创建文件对象
                并加入到文件对象列表
                """
                f = Duplicate_file(file, hash)
                duplicate_files.append(f)
        else:
            """第一次创建并添加"""
            f = Duplicate_file(file, hash)
            duplicate_files.append(f)

    else:
        """
        未发现重复文件
        存储将复制的文件列表
        以备复制
        """
        hashs.append(hash)
        files.append(file)

# 复制并命名排序
i = 1
for file in files:
    src_file = join(SRC_DIR, file)
    dst_file = join(DST_DIR, f'{i}.mp4')
    copy(src_file, dst_file)
    i += 1

# 报告
for f in duplicate_files:
    print(f"文件: {f.name}")
    print(f"hash: {f.hash}")
    print(f"重复次数: {f.times}")
    print("-----------------------------------")