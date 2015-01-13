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

class EventsTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.event import Event
        self.Event = Event
        self.assertIsNotNone(self.Event)

    def test_creating_an_event(self):
        e = self.Event()
        self.assertIsNotNone(e)

class CampaignTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.campaign import Campaign
        self.Campaign = Campaign
        self.assertIsNotNone(self.Campaign)

    def test_creating_a_campaign(self):
        c = self.Campaign('DnD')
        self.assertIsNotNone(c)
        self.assertEqual(c.name, 'DnD')

if __name__ == '__main__':
    unittest.main()

