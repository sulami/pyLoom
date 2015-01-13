#!/usr/bin/env python3
# coding: utf-8

import unittest

class ThreadTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.thread import Thread
        self.Thread = Thread
        self.assertIsNotNone(self.Thread)

    def test_creating_a_thread(self):
        t = self.Thread('t1')
        self.assertIsNotNone(t)
        self.assertEqual(t.name, 't1')

class ItemTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.item import Item
        self.Item = Item
        self.assertIsNotNone(self.Item)

    def test_creating_an_item(self):
        i = self.Item()
        self.assertIsNotNone(i)

if __name__ == '__main__':
    unittest.main()

