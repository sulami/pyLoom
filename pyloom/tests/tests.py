#!/usr/bin/env python3
# coding: utf-8

import unittest

from pyloom.campaign import Campaign
from pyloom.event import Event
from pyloom.session import Session
from pyloom.thread import Thread

class ThreadTestCase(unittest.TestCase):
    def test_creating_a_thread(self):
        t = Thread('t1')
        self.assertIsNotNone(t)
        self.assertEqual(t.name, 't1')

class SessionTestCase(unittest.TestCase):
    def test_creating_a_session(self):
        s = Session('s1')
        self.assertIsNotNone(s)
        self.assertEqual(s.name, 's1')

    def test_get_a_session(self):
        s1 = Session('s1')
        s2 = Session('s2')

        e1 = Event(s1)
        e2 = Event(s1)
        e3 = Event(s1)
        e4 = Event(s2)
        e5 = Event(s2)
        e6 = Event(s2)

        ses1 = s1.events
        self.assertEqual(ses1, [e1, e2, e3])

class EventsTestCase(unittest.TestCase):
    def test_creating_an_event(self):
        s = Session('s1')
        e = Event(s)
        self.assertIsNotNone(e)
        self.assertEqual(e.session, s)

class CampaignTestCase(unittest.TestCase):
    def test_creating_a_campaign(self):
        c = Campaign('DnD')
        self.assertIsNotNone(c)
        self.assertEqual(c.name, 'DnD')
        self.assertEqual(c.events, [])

    def test_adding_an_event(self):
        c = Campaign('DnD')
        c.add_event(None)
        self.assertEqual(c.events, [None, ])

    def test_adding_an_event_in_position(self):
        c = Campaign('DnD')
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

