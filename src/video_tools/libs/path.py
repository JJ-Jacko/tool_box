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
        