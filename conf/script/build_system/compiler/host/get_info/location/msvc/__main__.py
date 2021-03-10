#!/usr/bin/env python3

import cli_fetch_compiler_info

from cli import cli_find_msvc_installation_path

# Run as a script
if __name__ == '__main__':
    cli_fetch_compiler_info.cli_init()
    cli_find_msvc_installation_path()