from pathlib import Path
from typing import Generator


def iterdir_ext(
        path: Path,
        *exts: str
) -> Generator[Path, None, None]:
    """遍历文件夹下的指定拓展名的所有文件

    Args:
        path: 文件夹的路径
        exts: 拓展名

    Yields:
        file_path: 指定拓展名的文件
    """
    
    if not path.is_dir():
        raise ValueError("传入的路径必须为文件夹")

    for sub_p in path.iterdir():
        if not sub_p.is_file():
            continue
        if not sub_p.suffix:
            continue
        if sub_p.suffix[1:] not in exts:
            continue
        
        yield sub_p
        

def iterdir_recurse(path: Path) -> Generator[Path, None, None]:
    """递归遍历文件夹下的所有文件的路径

    Args:
        path (Path): 文件夹的路径

    Yields:
        file_path: 所有文件的路径
    """
    
    if not path.is_dir():
        raise ValueError("传入的路径必须为文件夹")
    
    for sub_p in path.iterdir():
        if sub_p.is_file():
            yield sub_p
        elif sub_p.is_dir():
            yield from iterdir_recurse(sub_p)
            