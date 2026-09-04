"""Some useful tools in box"""

import argparse
from pathlib import Path
from typing import Dict
from typing import Set

from tool_box import context
from tool_box.log import get_logger
from tool_box.services import compressed_files_extract
from tool_box.services import files_duplicate
from tool_box.services import files_rename
from tool_box.services import files_summary
from tool_box.services import images_color_reverse
from tool_box.services import images_to_pdf
from tool_box.services import videos_encoding
from tool_box.services import videos_to_gif


process_commands_map: Dict[str, function] = {
    "compressed_files_extract": compressed_files_extract.run,
    "files_duplicate": files_duplicate.run,
    "files_rename": files_rename.run,
    "files_summary": files_summary.run,
    "images_color_reverse": images_color_reverse.run,
    "images_to_pdf": images_to_pdf.run,
    "videos_encoding": videos_encoding.run,
    "videos_to_gif": videos_to_gif.run,
}

process_commands_with_extension: Set[str] = {
    "files_duplicate",
    "files_rename",
}


def process_add_arguments(
        parser: argparse.ArgumentParser,
        with_extension: bool = False
):
    parser.add_argument("-i", "--input", required=True, help="input directory")
    parser.add_argument("-o", "--output", required=False, help="output directory")

    if with_extension:
        parser.add_argument(
            "-ext", "--extension",
            dest="extensions",
            nargs="+",
            required=True,
            help="file extensions (e.g. jpg, txt, mp4)"
        )


def main():    
    logger = get_logger("tool-box", file=False)

    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command")
    parser_1 = subparsers.add_parser("compressed_files_extract", help=compressed_files_extract.__doc__)
    parser_2 = subparsers.add_parser("files_duplicate", help=files_duplicate.__doc__)
    parser_3 = subparsers.add_parser("files_rename", help=files_rename.__doc__)
    parser_4 = subparsers.add_parser("files_summary", help=files_summary.__doc__)
    parser_5 = subparsers.add_parser("images_color_reverse", help=images_color_reverse.__doc__)
    parser_6 = subparsers.add_parser("images_to_pdf", help=images_to_pdf.__doc__)
    parser_7 = subparsers.add_parser("videos_encoding", help=videos_encoding.__doc__)
    parser_8 = subparsers.add_parser("videos_to_gif", help=videos_to_gif.__doc__)
    parser_9 = subparsers.add_parser("generate", help="generate something to screen")
    process_add_arguments(parser_1)
    process_add_arguments(parser_2, with_extension=True)
    process_add_arguments(parser_3, with_extension=True)
    process_add_arguments(parser_4)
    process_add_arguments(parser_5)
    process_add_arguments(parser_6)
    process_add_arguments(parser_7)
    process_add_arguments(parser_8)
    args = parser.parse_args()

    if args.command in process_commands_map:
        # Check input directory
        path_input = Path(args.input)
        if not path_input.is_dir():
            parser.error(f"{path_input} is not directory")

        # Check output directory
        if args.output:
            path_output = Path(args.output)
            if path_output.exists():
                if not path_output.is_dir():
                    parser.error(f"{path_output} is not directory")
            else:
                path_output = context.OUTPUT_DIR
                path_output.mkdir(parents=True, exist_ok=True)
        else:
            path_output = context.OUTPUT_DIR
            path_output.mkdir(parents=True, exist_ok=True)

        command_args = {
            "path_input": path_input,
            "path_output": path_output,
        }

        if args.command in process_commands_with_extension:
            command_args["extensions"] = set(args.extensions)

        process_commands_map[args.command](**command_args)

    elif args.command == "generate":
        compressed_files_extract.run(path_input, path_output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


