import contextlib
from dataclasses import dataclass
from pathlib import Path

import build_system.compiler.build_option.sanitizer
import build_system.compiler.family
import build_system.compiler.installed_instance.compiler_instance
import ext.cmd_integrity
import ext.error.core.cls_def
import ext.error.utils.try_external_errors


@dataclass(order=True, frozen=True)
class GNUCompilerInstance(build_system.compiler.installed_instance.compiler_instance.CompilerInstance):
    executable_file: Path

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'executable_file', self.__get_executable_file_from_installation_dir())

    def __get_executable_file_from_installation_dir(self) -> Path:
        executable_file, exists = ext.cmd_integrity.get_cmd_path(cmd=self.compiler_family.value, dir_path=self.installation_dir)

        if not exists:
            raise ext.error.core.cls_def.CompilerNotFoundError()

        ext.error.utils.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=executable_file,
                                                                             external_errors_to_manage={(Exception,): ext.error.core.cls_def.CompilerNotFoundError})

        return executable_file

    def create_env_context_manager(self) -> contextlib.AbstractContextManager:
        import build_system.compiler.installed_instance.set_env_default_compiler
        return build_system.compiler.installed_instance.set_env_default_compiler.EnvDefaultCompiler(compiler=self)

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_location, compiler_instance_exists = ext.cmd_integrity.get_cmd_path(cmd=compiler_family.value)

        if not compiler_instance_exists:
            raise ext.error.core.cls_def.CompilerNotFoundError()

        compiler_installation_dir = compiler_location.parent

        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.GCC,
                build_system.compiler.family.CompilerFamily.CLANG]

    @staticmethod
    def get_supported_sanitizers() -> list[build_system.compiler.build_option.sanitizer.CompilerSanitizer]:
        return list(build_system.compiler.build_option.sanitizer.CompilerSanitizer)
