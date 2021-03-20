import abc
from typing import AnyStr

import colorama

import utils.error.meta


def format_error_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + message + colorama.Style.RESET_ALL


def format_success_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.GREEN + message + colorama.Style.RESET_ALL


class BaseFormattedErrorMixin(metaclass=utils.error.meta.ErrorMeta):

    def __init__(self, message: str, *args):
        super().__init__(self._format_msg(message), *args)

    @staticmethod
    @abc.abstractmethod
    def _format_msg(message: str) -> str:
        ...


class FormattedErrorMixin(BaseFormattedErrorMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _format_msg(message: str) -> str:
        return format_error_msg(message)


class FormattedSuccessMixin(BaseFormattedErrorMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _format_msg(message: str) -> str:
        return format_success_msg(message)
