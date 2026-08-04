import subprocess

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run():
    logger = get_logger("videos_to_gif")
    fps = 10
    scale = 300

    for src_file in iter_dir_file(context.INPUT_DIR, exts=context.EXTENSION.MEDIA):
        palette_file = context.OUTPUT_DIR / f"{src_file.stem}.png"
        gif_file = context.OUTPUT_DIR / f"{src_file.stem}.gif"

        cmd_gen_palette = [
            "ffmpeg",
            "-hide_banner",
            "-i", str(src_file),
            "-vf", f"fps={fps},scale={scale}:{scale}:flags=lanczos,palettegen",
            str(palette_file)
        ]
        cmd_gen_gif = [
            "ffmpeg",
            "-hide_banner",
            "-i", str(src_file),
            "-i", str(palette_file),
            "-filter_complex", f"fps={fps},scale={scale}:{scale}:flags=lanczos[x];[x][1:v]paletteuse",
            "-loop", "0",
            str(gif_file)
        ]
        
        subprocess.run(cmd_gen_palette, check=True)
        subprocess.run(cmd_gen_gif, check=True)
        logger.info(f"finished: {src_file}")
        