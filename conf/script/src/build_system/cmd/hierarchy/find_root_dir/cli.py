import argparse

import colorama

import build_system.cmd.hierarchy.find_root_dir
import ext.cli.try_cmd


def cli_find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description="Finds the project's root folder, where the "
                    f"'{colorama.Fore.LIGHTBLACK_EX}{build_system.cmd.hierarchy.find_root_dir.BUILD_SYSTEM_CONF_FILE_NAME}{colorama.Style.RESET_ALL}' folder is. "
                    'It searches recursively parent folders upwards.')

    arg_parser.parse_args()

    def cli_cmd():
        project_root = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
        print(project_root, end=str())

    ext.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
