__all__ = ['EnvDefaultCompiler']

import contextlib
import os
from typing import Final, Optional

from .compiler_instance import *

_CC: Final[str] = 'CC'
_CXX: Final[str] = 'CXX'


class EnvDefaultCompiler(contextlib.AbstractContextManager):
    previous_c_compiler: Optional[str]
    previous_cpp_compiler: Optional[str]
    compiler: CompilerInstance

    def __init__(self, compiler: CompilerInstance) -> None:
        super().__init__()
        self.compiler = compiler

    def __enter__(self):
        self.__cache_compilers()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__uncache_compilers()
        return False

    def get_env(self) -> dict[str, list[str]]:
        return {_CC: [self.compiler.get_c_compiler_name()],
                _CXX: [self.compiler.get_cpp_compiler_name()]}

    def __cache_compilers(self):
        self.__cache_c_compiler()
        self.__cache_cpp_compiler()

    def __uncache_compilers(self):
        self.__uncache_c_compiler()
        self.__uncache_cpp_compiler()

    def __cache_c_compiler(self):
        if _CC in os.environ:
            self.previous_c_compiler = os.environ[_CC]
        else:
            self.previous_c_compiler = None

        os.environ[_CC] = self.compiler.get_c_compiler_name()

    def __cache_cpp_compiler(self):
        if _CXX in os.environ:
            self.previous_cpp_compiler = os.environ[_CXX]
        else:
            self.previous_cpp_compiler = None

        os.environ[_CXX] = self.compiler.get_cpp_compiler_name()

    def __uncache_c_compiler(self):
        if self.previous_c_compiler is None:
            del os.environ[_CC]
        else:
            os.environ[_CC] = self.previous_c_compiler

    def __uncache_cpp_compiler(self):
        if self.previous_cpp_compiler is None:
            del os.environ[_CXX]
        else:
            os.environ[_CXX] = self.previous_cpp_compiler
