__all__ = ['BUILD_SYSTEM_NAME',
           'BUILD_SYSTEM_CONF_FILE_EXTENSION',
           'BUILD_SYSTEM_CONF_FILE_NAME']

from ._type_alias import *

BUILD_SYSTEM_NAME: TAlias_Name = 'meson'

BUILD_SYSTEM_CONF_FILE_EXTENSION: TAlias_Name = 'build'
BUILD_SYSTEM_CONF_FILE_NAME: TAlias_Name = f'{BUILD_SYSTEM_NAME}.{BUILD_SYSTEM_CONF_FILE_EXTENSION}'
