#!/usr/bin/env python3

__all__ = ['TestFetchMSVCVersion']

import unittest
from typing import Final
from unittest import mock
from unittest.mock import MagicMock

import build_system.cmd.compiler.host.get_info.version.msvc.impl
from ext.meta_prog.introspection import *


class TestFetchMSVCVersion(unittest.TestCase):

    @mock.patch('build_system.cmd.compiler.host.get_info.version.msvc.impl.vswhere')
    @mock.patch('build_system.cmd.compiler.host.get_info.version.msvc.impl.find_msvc_location')
    def test_no_arg_return_none(self, mock_find_location: MagicMock, mock_vswhere: MagicMock):
        expected_return_value: Final = None
        expected_find_location_args: Final = None
        expected_find_location_calls: Final = [mock.call.find_msvc_location(expected_find_location_args)]

        mock_find_location.return_value = expected_return_value

        return_value = build_system.cmd.compiler.host.get_info.version.msvc.impl.fetch_msvc_version()

        assert mock_find_location.mock_calls == expected_find_location_calls
        assert len(mock_vswhere.mock_calls) == 0

        assert return_value is expected_return_value

    @mock.patch('build_system.cmd.compiler.host.get_info.version.msvc.impl.Path')
    @mock.patch('build_system.cmd.compiler.host.get_info.version.msvc.impl.vswhere')
    @mock.patch('build_system.cmd.compiler.host.get_info.version.msvc.impl.find_msvc_location')
    def test_random_arg_return_none(self, mock_find_location: MagicMock, mock_vswhere: MagicMock, mock_path: MagicMock):
        expected_return_value: Final = None
        expected_find_location_args: Final = mock_path('../randompath')
        expected_find_location_calls: Final = [mock.call.find_location(expected_find_location_args)]

        mock_find_location.return_value = None

        return_value = build_system.cmd.compiler.host.get_info.version.msvc.impl.fetch_msvc_version(expected_find_location_args)

        assert mock_find_location.mock_calls == expected_find_location_calls
        assert len(mock_vswhere.mock_calls) == 0

        assert return_value is expected_return_value


if is_caller_main():
    unittest.main()
