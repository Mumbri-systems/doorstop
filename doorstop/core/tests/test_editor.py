
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: LGPL-3.0-only

"""Unit tests for the doorstop.core.tree module."""

import logging
import operator
import os
import tempfile
import unittest
from unittest.mock import MagicMock, Mock, patch

from doorstop.core import editor

from doorstop.common import DoorstopError, DoorstopInfo, DoorstopWarning
# from doorstop.core.builder import build
from doorstop.core.document import Document
from doorstop.core.tests import EMPTY, FILES, SYS, MockDocumentSkip, test_document

class Test_get_or_gen(unittest.TestCase):
    """Unit tests for get_or_gen()"""

    def test_get_or_gen_exists(self):
        """Verify 'get_or_gen()' ability to fetch information"""
        self.assertIsNotNone(editor.get_or_gen(self,"settings"))

    def test_get_or_gen_not_exists(self):
        """Verify 'get_or_gen()' ability to generate and save information if it is not found"""
        # save a datum that does not exist
        editor.get_or_gen(self,"foo",default="bar")
        self.assertEqual(editor.get_or_gen(self,"foo"),"bar")
    
    def test_get_or_gen_exists_nested(self):
        """Verify 'get_or_gen()' ability to fetch nested information"""
        # get a nested (list or dict) element that does exist
        # NOTE: assume that lists behave the same as dicts in this case
        self.assertIsNotNone(editor.get_or_gen(self,"settings['digits']"))

    def test_get_or_gen_not_exists_nested(self):
        """Verify 'get_or_gen()' ability to generate and save nested information if it is not found"""
        # save a nested element that does not exist
        editor.get_or_gen(self,"foo['foo2']",default="bar")
        self.assertEqual(editor.get_or_gen(self,"foo['foo2']"),"bar")
        # NOTE: no test of editor!