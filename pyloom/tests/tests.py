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

class SessionTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.session import Session
        self.session = Session
        self.assertIsNotNone(self.session)

    def test_creating_a_session(self):
        s = self.session('s1')
        self.assertIsNotNone(s)
        self.assertEqual(s.name, 's1')

class EventsTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.event import Event
        self.Event = Event
        self.assertIsNotNone(self.Event)

    def test_creating_an_event(self):
        e = self.Event('session')
        self.assertIsNotNone(e)
        self.assertEqual(e.session, 'session')

class CampaignTestCase(unittest.TestCase):
    def setUp(self):
        from pyloom.campaign import Campaign
        self.Campaign = Campaign
        self.assertIsNotNone(self.Campaign)

    def test_creating_a_campaign(self):
        c = self.Campaign('DnD')
        self.assertIsNotNone(c)
        self.assertEqual(c.name, 'DnD')
        self.assertEqual(c.events, [])

    def test_adding_an_event(self):
        c = self.Campaign('DnD')
        c.add_event(None)
        self.assertEqual(c.events, [None, ])

    def test_adding_an_event_in_position(self):
        c = self.Campaign('DnD')
        c.add_event(1)
        self.assertEqual(c.events, [1, ])
        c.add_event(2, pos=0)
        self.assertEqual(c.events, [2, 1])
        c.add_event(3, pos=1)
        self.assertEqual(c.events, [2, 3, 1])
        c.add_event(4)
        self.assertEqual(c.events, [2, 3, 1, 4])

if __name__ == '__main__':
    unittest.main()

