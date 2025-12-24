"""合并图片成 pdf"""
from pathlib import Path

from PIL import Image

from video_tools.libs.path import iter_dir_file


INPUT_DIR = Path("INPUT")
OUTPUT_DIR = Path("OUTPUT")
IMAGE_EXTENSIONS = ("jpg", "png")

images = [
    Image.open(src_file).convert("RGB")
    for src_file in iter_dir_file(INPUT_DIR, exts=IMAGE_EXTENSIONS)
]

images[0].save(
    OUTPUT_DIR / f"output.pdf",
    save_all=True,
    append_images=images[1:]
)
