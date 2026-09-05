"""Some useful tools in box"""

import argparse
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Set

from tool_box import context
from tool_box.datas import Command
from tool_box.log import get_logger
from tool_box.services import compressed_files_extract
from tool_box.services import files_duplicate
from tool_box.services import files_rename
from tool_box.services import files_summary
from tool_box.services import images_color_reverse
from tool_box.services import images_to_pdf
from tool_box.services import videos_encoding
from tool_box.services import videos_to_gif


process_commands_map: Dict[str, Command] = {
    "compressed_files_extract": Command(
        func=compressed_files_extract.run,
        help=compressed_files_extract.__doc__,
        with_input=True,
        with_output=True,
        with_extension=False
    ),
    "files_duplicate": Command(
        func=files_duplicate.run,
        help=files_duplicate.__doc__,
        with_input=True,
        with_output=True,
        with_extension=True
    ),
    "files_rename": Command(
        func=files_rename.run,
        help=files_rename.__doc__,
        with_input=True,
        with_output=True,
        with_extension=True
    ),
    "files_summary": Command(
        func=files_summary.run,
        help=files_summary.__doc__,
        with_input=True,
        with_output=False,
        with_extension=False
    ),
    "images_color_reverse": Command(
        func=images_color_reverse.run,
        help=images_color_reverse.__doc__,
        with_input=True,
        with_output=True,
        with_extension=False
    ),
    "images_to_pdf": Command(
        func=images_to_pdf.run,
        help=images_to_pdf.__doc__,
        with_input=True,
        with_output=True,
        with_extension=False
    ),
    "videos_encoding": Command(
        func=videos_encoding.run,
        help=videos_encoding.__doc__,
        with_input=True,
        with_output=True,
        with_extension=False
    ),
    "videos_to_gif": Command(
        func=videos_to_gif.run,
        help=videos_to_gif.__doc__,
        with_input=True,
        with_output=True,
        with_extension=False,
        with_fps=True
    ),
    "generate": Command(
        func=None,
        help="generate something to screen",
        with_input=False,
        with_output=False,
        with_extension=False
    )
}


def register_commands(subparsers: argparse._SubParsersAction):
    for name, cmd in process_commands_map.items():
        parser = subparsers.add_parser(name, help=cmd.help)

        if cmd.with_input:
            parser.add_argument("-i", "--input", required=True, help="input directory")

        if cmd.with_output:
            parser.add_argument("-o", "--output", required=False, help="output directory")

        if cmd.with_extension:
            parser.add_argument(
                "-ext", "--extension",
                dest="extensions",
                nargs="+",
                required=True,
                help="file extensions (e.g. jpg, txt, mp4)"
            )

        if cmd.with_fps:
            parser.add_argument(
                "-fps", "--frame-rate",
                dest="fps",
                type=int,
                required=False,
                help="frame rate of target GIF image"
            )


def get_command_args(
        command_name: str,
        main_parser: argparse.ArgumentParser,
        main_parser_args: argparse.Namespace
):
    cmd: Command = process_commands_map.get(command_name)
    command_args: Dict[str, Any] = dict()
    
    if cmd.with_input:
        # Check input directory
        path_input = Path(main_parser_args.input)
        if not path_input.is_dir():
            main_parser.error(f"{path_input} is not directory")

        command_args["path_input"] = path_input

    if cmd.with_output:
        # Check output directory
        if main_parser_args.output:
            path_output = Path(main_parser_args.output)
            if path_output.exists():
                if not path_output.is_dir():
                    main_parser.error(f"{path_output} is not directory")
            else:
                path_output = context.OUTPUT_DIR
                path_output.mkdir(parents=True, exist_ok=True)
        else:
            path_output = context.OUTPUT_DIR
            path_output.mkdir(parents=True, exist_ok=True)

        command_args["path_output"] = path_output

    if cmd.with_extension:
        command_args["extensions"] = set(main_parser_args.extensions)

    if cmd.with_fps:
        if fps := main_parser_args.fps:
            command_args["fps"] = fps

    return command_args


def main():
    logger = get_logger("tool-box", file=False)

    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command")
    register_commands(subparsers)
    args = parser.parse_args()

    if not (command_name := args.command):
        parser.print_help()
        return

    cmd_args = get_command_args(command_name, parser, args)
    cmd = process_commands_map.get(command_name)
    cmd.func(**cmd_args)


if __name__ == "__main__":
    main()
