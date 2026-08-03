"""合并图片成 pdf"""

from PIL import Image

from tool_box import context
from tool_box.path import iter_dir_file


def run():
    images = [
        Image.open(src_file).convert("RGB")
        for src_file in iter_dir_file(context.INPUT_DIR, exts=context.EXTENSION.IMAGE)
    ]

    images[0].save(
        context.OUTPUT_DIR / f"output.pdf",
        save_all=True,
        append_images=images[1:]
    )
