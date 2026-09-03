"""merge all images files to PDF file"""

from pathlib import Path

from PIL import Image

from tool_box import context
from tool_box.path import iter_dir_file


def run(
        path_input: Path,
        path_output: Path
):
    images = [
        Image.open(src_file).convert("RGB")
        for src_file in iter_dir_file(path_input, exts=context.EXTENSION.IMAGE)
    ]

    images[0].save(
        path_output / f"output.pdf",
        save_all=True,
        append_images=images[1:]
    )
