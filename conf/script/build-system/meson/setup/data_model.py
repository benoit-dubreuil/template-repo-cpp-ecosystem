from enum import Enum, IntFlag, unique


@unique
class Architecture(IntFlag):
    UNKNOWN = 0
    A_16 = 2 ** 4
    A_32 = 2 ** 5
    A_64 = 2 ** 6
    A_128 = 2 ** 7


@unique
class Compiler(Enum):
    MSVC = 'msvc'
    CLANG = 'clang'
    GCC = 'gcc'


@unique
class BuildType(Enum):
    DEBUG = 'debug'
    DEBUG_OPTIMIZED = 'debugoptimized'
    RELEASE = 'release'


@unique
class OSFamily(Enum):
    WINDOWS = 'windows'
    DARWIN = 'darwin'
    LINUX = 'linux'


@unique
class SupportedCompilersByOSFamily(Enum):
    OSFamily.WINDOWS = [Compiler.MSVC, Compiler.CLANG, Compiler.GCC]
    OSFamily.DARWIN = [Compiler.CLANG, Compiler.GCC]
    OSFamily.LINUX = [Compiler.CLANG, Compiler.GCC]