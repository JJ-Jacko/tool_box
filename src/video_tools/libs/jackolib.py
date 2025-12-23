import hashlib


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
