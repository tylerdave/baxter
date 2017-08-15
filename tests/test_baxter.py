#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_baxter
----------------------------------

Tests for `baxter` module.
"""

import unittest

import baxter


class TestBaxter(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(baxter.__version__)

    def tearDown(self):
        pass
