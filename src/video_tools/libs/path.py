import hashlib
from pathlib import Path
from typing import Generator
from typing import Tuple


def iter_dir_file(
        path: Path,
        recurse: bool = False,
        exts: Tuple[str | None] = ()
) -> Generator[Path, None, None]:
    """遍历文件夹下的文件

    Args:
        path: 文件夹的路径
        recurse: 是否遍历所有子文件夹
        exts: 拓展名 用于获取指定拓展名的文件

    Yields:
        file_path: 指定拓展名的文件的路径
    """
    
    if not path.is_dir():
        raise ValueError("传入的路径必须为文件夹")
    
    for sub_p in path.iterdir():
        if sub_p.is_dir() and recurse:
            yield from iter_dir_file(sub_p, recurse, exts)

        if not sub_p.is_file():
            continue
        
        if exts:
            # 文件无拓展名
            if not sub_p.suffix:
                continue
            # 文件拓展名不符合条件
            if sub_p.suffix[1:] not in exts:
                continue
        
        yield sub_p


def get_file_hash(
        file_path: Path,
        algorithm: str = "MD5"
):
    """获取文件的哈希值

    Args:
        file_path: 文件的的路径
        algorithm: 算法类型 默认 `MD5`
    """
    
    if not file_path.is_file():
        raise ValueError("传入的路径必须为文件")
    
    hash_obj = hashlib.new(algorithm)

    # 读取文件块并更新哈希对象
    with file_path.open("rb") as f:
        while chunk := f.read(4096): # 4096 字节为一个块
            hash_obj.update(chunk)

    
    # 获取十六进制形式的哈希值
    return hash_obj.hexdigest()
