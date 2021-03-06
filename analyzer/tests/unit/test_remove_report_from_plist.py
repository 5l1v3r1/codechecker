# -----------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -----------------------------------------------------------------------------

""" Unit tests for removing report from plist by using skip file. """

import os
import unittest

from codechecker_common import skiplist_handler
from codechecker_common.plist_parser import remove_report_from_plist

OLD_PWD = None


def setup_module():
    """ Change to the directory with sample version outputs. """
    global OLD_PWD
    OLD_PWD = os.getcwd()
    os.chdir(os.path.join(os.path.dirname(__file__),
             'remove_report_test_files'))


def teardown_module():
    """ Restore the current working directory. """
    global OLD_PWD
    os.chdir(OLD_PWD)


class TestRemoveReportFromPlist(unittest.TestCase):
    """ Test skipping header files. """

    def test_skip_x_header(self):
        """ Test skipping a header file. """
        with open('skip_x_header.txt',
                  encoding="utf-8", errors="ignore") as skip_file:
            skip_handler = skiplist_handler.SkipListHandler(skip_file.read())

        with open('x.plist', 'rb') as plist_data:
            data = remove_report_from_plist(plist_data, skip_handler)

        with open('skip_x_header.expected.plist', 'rb') as plist_file:
            expected = plist_file.read()

        self.assertEqual(data, expected)

    def test_skip_all_header(self):
        """ Test skipping all header files. """
        with open('skip_all_header.txt',
                  encoding="utf-8", errors="ignore") as skip_file:
            skip_handler = skiplist_handler.SkipListHandler(skip_file.read())

        with open('x.plist', 'r') as plist_data:
            data = remove_report_from_plist(plist_data, skip_handler)

        with open('skip_all_header.expected.plist', 'rb') as plist_file:
            expected = plist_file.read()

        self.assertEqual(data, expected)
