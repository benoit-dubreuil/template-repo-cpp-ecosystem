import argparse
import sys
import typing

import utils.error.meta
import utils.error.status


class ExitCLIError(metaclass=utils.error.meta.ErrorMeta):

    def exit_cli(self, arg_parser: argparse.ArgumentParser, print_usage: bool = False) -> typing.NoReturn:
        assert isinstance(self, utils.error.status.EncodedError)

        if print_usage:
            arg_parser.print_usage(sys.stderr)

        arg_parser.exit(self.get_error_status(), str(self))

    def raise_or_exit_cli(self, arg_parser: argparse.ArgumentParser, print_usage: bool = False) -> typing.NoReturn:
        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            self.exit_cli(arg_parser, print_usage)
        else:
            raise self