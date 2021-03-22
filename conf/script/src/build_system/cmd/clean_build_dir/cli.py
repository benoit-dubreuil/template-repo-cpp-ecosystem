import argparse
from typing import Final

import build_system.cmd.hierarchy.find_build_dir
import utils.cli.arg
import utils.cli.arg_parsing
import utils.cli.try_cmd
from utils.more_typing import AnyPath

ROOT_DIR_ARG: Final[utils.cli.arg.CLIArg] = utils.cli.arg.CLIArg('rootdir')


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's {build_system.cmd.hierarchy.find_build_dir.BUILD_DIR_NAME} folder, where the build system organizes into subfolders specific builds.")
    utils.cli.arg_parsing.add_optional_path_arg(arg_parser, ROOT_DIR_ARG, path_arg_help=f"The project's root directory")

    root_dir: AnyPath = utils.cli.arg_parsing.parse_optional_path_arg(arg_parser, ROOT_DIR_ARG)

    def cli_cmd():
        build_system.cmd.clean_build_dir.clean_build_dir(build_dir=root_dir)

    utils.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
