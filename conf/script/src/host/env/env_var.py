import collections.abc
import os
import typing
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Final

from utils.more_typing import PathLike

_ENV_VAR_ITEM_COUNT: Final[int] = 1

_T_Key = PathLike
_T_Single_Value = PathLike
_T_Values = list[_T_Single_Value]


@dataclass(init=False, order=True)
class EnvVar(collections.abc.Mapping[_T_Key, _T_Values]):
    __env_key: _T_Key
    __env_values: _T_Values

    def __init__(self, key_name=None, values=None) -> None:
        self.__env_key = key_name if key_name is not None else str()
        self.__env_values = values if values is not None else _T_Values()

    def get_env_key(self) -> _T_Key:
        return self.__env_key

    def get_env_values(self) -> _T_Values:
        return self.__env_values

    def __contains__(self, key: _T_Key) -> bool:
        self.__verify_key_type(key=key)
        env_key: _T_Key = self.get_env_key()

        return key is env_key or key == env_key

    def __getitem__(self, key: _T_Key) -> _T_Values:
        if key not in self:
            raise KeyError()

        return self.get_env_values()

    def __len__(self) -> int:
        return _ENV_VAR_ITEM_COUNT

    def __iter__(self) -> Iterator[_T_Key]:
        # TODO
        ...

    def __str__(self) -> str:
        assert self.__env_key is not None
        assert self.__env_values is not None

        joined_values = self.join_values()

        return f'{self.get_env_key()}={joined_values}'

    def join_values(self) -> str:
        return os.pathsep.join(self.get_env_values())

    @staticmethod
    def __verify_key_type(key: _T_Key) -> None:
        if not isinstance(key, typing.get_args(_T_Key)):
            raise TypeError()

    @staticmethod
    def __verify_single_value_type(single_value: _T_Single_Value) -> None:
        if not isinstance(single_value, typing.get_args(_T_Single_Value)):
            raise TypeError()

    @staticmethod
    def __verify_values_type(values: _T_Values) -> None:
        if not isinstance(values, typing.get_args(_T_Values)):
            raise TypeError()
