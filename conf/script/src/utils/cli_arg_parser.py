import argparse
import sys
from pathlib import Path
from typing import AnyStr, Final, Optional
from utils.more_typing import AnyPath

import utils.cli_error
import utils.formatted_error

DEFAULT_PATH_ARG_NAME: Final[str] = 'path'
DEFAULT_PATH_ARG: Final[str] = '-' + DEFAULT_PATH_ARG_NAME


def add_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: AnyStr = DEFAULT_PATH_ARG, path_arg_default_value: AnyPath = None,
                          path_arg_help: Optional[AnyStr] = None):
    arg_parser.add_argument(path_arg, type=Path, nargs=argparse.OPTIONAL, const=path_arg_default_value, default=path_arg_default_value, help=path_arg_help)


def _assure_no_unknown_parsed_args(arg_parser: argparse.ArgumentParser, unknown_parsed_args: list[str]):
    if len(unknown_parsed_args) > 0:
        error = utils.cli_error.UnknownParsedArgError(unknown_parsed_args)

        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            arg_parser.print_usage(sys.stderr)
            arg_parser.exit(utils.cli_error.ErrorStatus.UNKNOWN_PARSED_ARG, str(error))
        else:
            raise error


def _assure_nonempty_parsed_path(arg_parser: argparse.ArgumentParser, path_arg: str, parsed_path: AnyPath):
    if str(parsed_path) == str():
        error = utils.cli_error.EmptyParsedArgError(path_arg)

        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            arg_parser.print_usage(sys.stderr)
            arg_parser.exit(utils.cli_error.ErrorStatus.EMPTY_PARSED_ARG, str(error))
        else:
            raise error


def parse_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: str = DEFAULT_PATH_ARG) -> AnyPath:
    parsed_args, unknown_parsed_args = arg_parser.parse_known_args([path_arg])
    _assure_no_unknown_parsed_args(arg_parser, unknown_parsed_args)
    parsed_path: AnyPath = getattr(parsed_args, path_arg) if path_arg in parsed_args else None
    _assure_nonempty_parsed_path(arg_parser, path_arg, parsed_path)

    return parsed_path