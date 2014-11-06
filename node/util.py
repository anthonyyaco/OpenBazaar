import os
import sys
import platform


def is_mac():
    os_name = platform.uname()[0]
    return os_name == 'Darwin'


def osx_check_dyld_library_path():
    """This is a necessary workaround as you cannot set the DYLD_LIBRARY_PATH
    by the time python has started."""
    if not os.environ.get('DYLD_LIBRARY_PATH'):
        print (
            'WARNING: DYLD_LIBRARY_PATH not set, this might cause issues'
            '\nwith openssl elliptic curve cryptography and other libraries.'
            '\nIt is recommended that you stop OpenBazaar and set your'
            '\nDYLD_LIBRARY_PATH environment variable as follows:'
            '\n    export DYLD_LIBRARY_PATH=$(brew --prefix openssl)/'
            'lib:${DYLD_LIBRARY_PATH}'
            '\nthen restart OpenBazaar.'
        )
        sys.exit(1)
