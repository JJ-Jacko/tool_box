import hashlib
import os
import os.path as op


def lsdirr(path):
    """
    返回指定目录及子目录下
    文件列表
    """
    file_paths = [] #存储文件路径的列表
    # 遍历目录
    for root, dirs, files in os.walk(path):
        for file in files:
            # 将文件的完整路径添加到列表中
            file_paths.append(op.relpath(op.join(root, file), path))
    return file_paths


def lsdirr_af(path, file_extension):
    """
    返回指定目录及子目录下
    指定文件后缀的文件列表
    """
    appointed_extension_file_paths = []
    files = lsdirr(path)

    for file in files:
        if op.splitext(file)[1][1:] == file_extension:
            appointed_extension_file_paths.append(file)
    
    return appointed_extension_file_paths


def calc_file_hash(file, algorithm='sha256'):
    """
    计算文件的哈希值
    哈希算法默认'sha256'
    """
    # 创建哈希对象
    hash_obj = hashlib.new(algorithm)

    # 以二进制模式打开文件
    with open(file, 'rb') as f:
        # 读取文件块并更新哈希对象
        while chunk := f.read(4096):  #4096字节为一个块
            hash_obj.update(chunk)

    # 获取十六进制形式的哈希值
    hash = hash_obj.hexdigest()
    return hash
