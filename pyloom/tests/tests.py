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
        self.assertEqual(t.items, [])

    def test_adding_an_item(self):
        t = self.Thread('t1')
        i = object()
        t.add_item(i)
        self.assertIn(i, t.items)

if __name__ == '__main__':
    unittest.main()

