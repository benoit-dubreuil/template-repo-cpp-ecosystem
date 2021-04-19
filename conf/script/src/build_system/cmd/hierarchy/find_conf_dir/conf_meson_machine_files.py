from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.consts
import ext.error.core.cls_def
import ext.error.utils.try_external_errors


def get_meson_machine_files_dir_path_relative_to_build_system_dir(conf_build_system_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.find_conf_dir.conf_build_system

    if conf_build_system_dir is None:
        conf_build_system_dir = build_system.cmd.hierarchy.find_conf_dir.conf_build_system.find_conf_build_system_dir()

    return conf_build_system_dir / build_system.cmd.hierarchy.consts.MESON_MACHINE_FILES_DIR_NAME


def find_meson_machine_files_dir(conf_build_system_dir: Optional[Path] = None) -> Path:
    meson_machine_files_dir = get_meson_machine_files_dir_path_relative_to_build_system_dir(conf_build_system_dir=conf_build_system_dir)

    ext.error.utils.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=meson_machine_files_dir,
                                                                         external_errors_to_manage={(Exception,): ext.error.core.cls_def.MesonMachineFilesDirNotFoundError})

    meson_machine_files_dir = meson_machine_files_dir.absolute()

    if not meson_machine_files_dir.is_dir():
        raise ext.error.core.cls_def.ConfBuildSystemDirNotFoundError()

    return meson_machine_files_dir
