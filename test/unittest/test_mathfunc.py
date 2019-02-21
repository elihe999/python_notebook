#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from math_suite.mathfunc import add

class TestMathFunc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, add(1,2))
        self.assertNotEqual(3, add(2,2))


if __name__ == '__main__':
    unittest.main()
