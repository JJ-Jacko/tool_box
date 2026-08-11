import ffmpeg

from tool_box import context
from tool_box.log import get_logger
from tool_box.path import iter_dir_file


def run():
    logger = get_logger("encoding_media")

    for src_file in iter_dir_file(context.INPUT_DIR, exts=context.EXTENSION.MEDIA):
        dst_file = context.OUTPUT_DIR / f"{src_file.stem}.mp4"

        input_stream = ffmpeg.input(src_file)
        output_stream = (
            input_stream
            .output(filename=dst_file, vcodec="libx264")
        )

        output_stream.run(overwrite_output=True, quiet=True)
        logger.info(f"finished: {str(src_file)}")
        