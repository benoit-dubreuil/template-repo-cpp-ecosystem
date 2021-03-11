from pathlib import Path
from typing import NoReturn, Optional, Union

from build_system.compiler.compiler import Compiler
from build_system.compiler.version import CompilerVersion

from build_system.compiler.host.get_info.cli import cli_fetch_compiler_info

from build_system.compiler.host.get_info import location
import build_system.compiler.host.get_info.location.msvc.cli

from build_system.compiler.host.get_info import version
import build_system.compiler.host.get_info.version.msvc.fetch_msvc_version


def _fetch_version_no_arg(compiler_installation_path: Optional[Path] = None) -> Union[CompilerVersion, NoReturn]:
    compiler_version: Optional[CompilerVersion] = version.msvc.fetch_msvc_version.fetch(compiler_installation_path)

    if compiler_version is None:
        location.msvc.cli.error_compiler_not_found()

    return compiler_version


def fetch_version() -> None:
    cli_fetch_compiler_info(Compiler.MSVC, _fetch_version_no_arg, help_path_meaning='installation')
