__all__ = ['HiddenPrints']

import contextlib
import os
import sys


# From: https://stackoverflow.com/a/45669280/2924010
class HiddenPrints(contextlib.AbstractContextManager):

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.close()
        sys.stdout = self._original_stdout
