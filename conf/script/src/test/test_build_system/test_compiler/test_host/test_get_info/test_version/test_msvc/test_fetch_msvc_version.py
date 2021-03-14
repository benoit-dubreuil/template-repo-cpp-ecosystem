#!/usr/bin/env python3

import unittest
from typing import Final
from unittest import mock
from unittest.mock import MagicMock

from build_system.compiler.host.get_info.version.msvc import fetch_msvc_version


class TestFetch(unittest.TestCase):

    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.vswhere')
    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.msvc.installation_path')
    def test_no_arg_return_none(self, mock_installation_path: MagicMock, mock_vswhere: MagicMock):
        expected_return_value: Final = None
        expected_installation_path_args: Final = None
        expected_installation_path_calls: Final = [mock.call.find(expected_installation_path_args)]

        mock_installation_path.find.return_value = expected_return_value

        return_value = fetch_msvc_version.fetch()

        assert mock_installation_path.mock_calls == expected_installation_path_calls
        assert len(mock_vswhere.mock_calls) == 0

        assert return_value is expected_return_value

    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.Path')
    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.vswhere')
    @mock.patch('build_system.compiler.host.get_info.version.msvc.fetch_msvc_version.msvc.installation_path')
    def test_random_arg_return_none(self, mock_installation_path: MagicMock, mock_vswhere: MagicMock, mock_path: MagicMock):
        expected_return_value: Final = None
        expected_installation_path_args: Final = mock_path('../randompath')
        expected_installation_path_calls: Final = [mock.call.find(expected_installation_path_args)]

        mock_installation_path.find.return_value = None

        return_value = fetch_msvc_version.fetch(expected_installation_path_args)

        assert mock_installation_path.mock_calls == expected_installation_path_calls
        assert len(mock_vswhere.mock_calls) == 0

        assert return_value is expected_return_value

# TODO : Add more tests