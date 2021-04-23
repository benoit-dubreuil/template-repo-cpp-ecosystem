import argparse
from typing import Optional, Union

from .format import *
from .managed import *
from .status import *
from ...meta_prog.encapsulation import *


@export
@ManageClass(error_formatter_cls=FormattedSuccessMixin, encoded_error_status=ErrorStatus.SUCCESS)
class SuccessWarning(UserWarning):

    def __init__(self):
        super().__init__('Success')


@export
@ManageClass(encoded_error_status=ErrorStatus.UNSUPPORTED)
class UnsupportedError(RuntimeError):

    def __init__(self, original_raised_error: Optional[BaseException] = None):
        error_msg = 'Unsupported error'

        if original_raised_error is not None:
            error_msg += '\n'
            error_msg += str(original_raised_error)

        super().__init__('Unsupported error')

        if original_raised_error is not None:
            self.with_traceback(original_raised_error.__traceback__)


@export
@ManageClass(encoded_error_status=ErrorStatus.ARG_PARSER)
class ArgParserError(RuntimeError):

    def __init__(self, arg_parser_exception: Union[argparse.ArgumentError, argparse.ArgumentTypeError]):
        error_msg = 'Argument parser error'
        arg_parser_error_msg = str(arg_parser_exception)

        if arg_parser_error_msg != str() and arg_parser_error_msg != str(None):
            error_msg += '\n'
            error_msg += arg_parser_error_msg

        super().__init__(error_msg)


@export
@ManageClass(encoded_error_status=ErrorStatus.UNKNOWN_PARSED_ARG)
class UnknownParsedArgError(TypeError):

    def __init__(self, unknown_parsed_args: list[str]):
        super().__init__(f"Unsupported argument '{unknown_parsed_args}'")


@export
@ManageClass(encoded_error_status=ErrorStatus.EMPTY_PARSED_ARG)
class EmptyParsedArgError(ValueError):

    def __init__(self, arg: str):
        super().__init__(f"'{arg}' argument must be followed by a path string")


@export
@ManageClass(encoded_error_status=ErrorStatus.ROOT_DIR_NOT_FOUND)
class RootDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Root directory not found')


@export
@ManageClass(encoded_error_status=ErrorStatus.BUILD_DIR_NOT_FOUND)
class BuildDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Build directory not found')


@export
@ManageClass(encoded_error_status=ErrorStatus.BUILD_DIR_NOT_DIR)
class BuildDirNotDirError(FileExistsError):

    def __init__(self):
        super().__init__("Build directory exists but isn't a directory")


@export
@ManageClass(encoded_error_status=ErrorStatus.BUILD_DIR_NOT_EMPTY)
class BuildDirNotEmptyError(FileExistsError):

    def __init__(self):
        super().__init__("Build directory isn't empty")


@export
@ManageClass(encoded_error_status=ErrorStatus.CONF_DIR_NOT_FOUND)
class ConfDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Conf directory not found')


@export
@ManageClass(encoded_error_status=ErrorStatus.CONF_BUILD_SYSTEM_DIR_NOT_FOUND)
class ConfBuildSystemDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Build system directory inside the conf directory not found')


@export
@ManageClass(encoded_error_status=ErrorStatus.MESON_MAIN_FILE_NOT_FOUND)
class MesonMainFileNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__("Meson's (build system) main file, i.e. Meson's standalone executable, not found.")


@export
@ManageClass(encoded_error_status=ErrorStatus.MESON_MACHINE_FILES_DIR_NOT_FOUND)
class MesonMachineFilesDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__("Meson's (build system) machine files directory inside the conf build system directory not found")


@export
@ManageClass(encoded_error_status=ErrorStatus.COMPILER_REQS_NOT_FOUND)
class CompilerReqsNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Compiler requirements configuration file not found')


@export
@ManageClass(encoded_error_status=ErrorStatus.COMPILER_NOT_FOUND)
class CompilerNotFoundError(FileNotFoundError):

    def __init__(self, error_msg: str = 'Compiler at the supplied path does not exist or requires ungranted permissions'):
        super().__init__(error_msg)


@export
class NoSupportedCompilersAvailableError(CompilerNotFoundError):

    def __init__(self):
        super().__init__(error_msg='No supported compilers are available')

    @staticmethod
    def get_error_status() -> ErrorStatus:
        return ErrorStatus.NO_SUPPORTED_COMPILERS_AVAILABLE


@export
@ManageClass(encoded_error_status=ErrorStatus.MSVC_COMPILER_VCVARS_DIR_NOT_FOUND)
class MSVCCompilerVcvarsDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('MSVC compiler vcvars directory not found')


@export
@ManageClass(encoded_error_status=ErrorStatus.MSVC_COMPILER_VCVARS_BATCH_FILE_NOT_FOUND)
class MSVCCompilerVcvarsBatchFileNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('MSVC compiler vcvars batch file for supported architecture not found')