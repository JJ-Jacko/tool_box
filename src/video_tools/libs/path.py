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
        