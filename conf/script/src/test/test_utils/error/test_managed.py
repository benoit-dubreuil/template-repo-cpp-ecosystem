#!/usr/bin/env python3

import unittest

import utils.cli.main
import utils.error.format
import utils.error.meta
import utils.error.status
from utils.error.managed import ManageClass


class TestManage(unittest.TestCase):

    def assert_decorated_error_type(self, decorated_error_cls: type):
        self.assertEqual(type(decorated_error_cls), utils.error.meta.ErrorMeta)
        self.assertIsInstance(decorated_error_cls(), utils.error.managed.ManagedError)
        self.assertNotIsInstance(decorated_error_cls(), utils.error.managed.ManageClass)

    def test_decorate_error(self):
        @ManageClass
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.status.ErrorStatus:
                return utils.error.status.ErrorStatus.UNSUPPORTED

        self.assert_decorated_error_type(DecoratedError)

    def test_raise_decorated_error(self):
        @ManageClass
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.status.ErrorStatus:
                return utils.error.status.ErrorStatus.UNSUPPORTED

        with self.assertRaises(DecoratedError):
            raise DecoratedError()

    def test_error_status_of_raised_decorated_error(self):
        @ManageClass
        class DecoratedError(RuntimeError):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.status.ErrorStatus:
                return utils.error.status.ErrorStatus.UNSUPPORTED

        with self.assertRaises(DecoratedError) as context_manager:
            raise DecoratedError()

        raised_exception = context_manager.exception
        self.assertEqual(raised_exception.get_error_status(), utils.error.status.ErrorStatus.UNSUPPORTED)

    def test_decorate_warning(self):
        @ManageClass
        class DecoratedError(RuntimeWarning):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.status.ErrorStatus:
                return utils.error.status.ErrorStatus.UNSUPPORTED

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter(self):
        @ManageClass(error_formatter_cls=utils.error.format.FormattedSuccess)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

            @staticmethod
            def get_error_status() -> utils.error.status.ErrorStatus:
                return utils.error.status.ErrorStatus.SUCCESS

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)

    def test_decorate_success_with_formatter_and_status(self):
        @ManageClass(error_formatter_cls=utils.error.format.FormattedSuccess, encoded_error_status=utils.error.status.ErrorStatus.SUCCESS)
        class DecoratedError(UserWarning):

            def __init__(self):
                super().__init__(str(unittest))

        DecoratedError()
        self.assert_decorated_error_type(DecoratedError)


if utils.cli.main.is_caller_main():
    unittest.main()