#!/usr/bin/env python3
# coding: utf-8

import unittest

class ThreadTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.thread import Thread
        self.Thread = Thread
        self.assertIsNotNone(self.Thread)

    def test_stuff(self):
        t = self.Thread()
        self.assertIsNotNone(t)

if __name__ == '__main__':
    unittest.main()

