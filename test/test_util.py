import os
import platform
import unittest

import mock

from node import util


class TestUtil(unittest.TestCase):

    @mock.patch.object(platform, 'uname', lambda: ['Darwin'])
    def test_is_mac_Darwin(self):
        self.assertTrue(util.is_mac())

    @mock.patch.object(platform, 'uname', lambda: ['Linux'])
    def test_is_mac_Linux(self):
        self.assertFalse(util.is_mac())

    @mock.patch.object(platform, 'uname', lambda: ['Windows'])
    def test_is_mac_Windows(self):
        self.assertFalse(util.is_mac())

    @mock.patch.object(os, 'environ', {})
    def test_osx_check_dyld_library_path_None(self):
        self.assertRaises(
            SystemExit,
            util.osx_check_dyld_library_path
        )

    @mock.patch.object(os, 'environ', {'DYLD_LIBRARY_PATH': False})
    def test_osx_check_dyld_library_path_False(self):
        self.assertRaises(
            SystemExit,
            util.osx_check_dyld_library_path
        )

    @staticmethod
    @mock.patch.object(os, 'environ', {'DYLD_LIBRARY_PATH': True})
    def test_osx_check_dyld_library_path_True():
        util.osx_check_dyld_library_path()


if __name__ == '__main__':
    unittest.main()
