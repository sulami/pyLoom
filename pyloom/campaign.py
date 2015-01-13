class Campaign(object):
    """Holds all events in a given campaign"""

    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event, pos=-1):
        if pos == -1:
            self.events.append(event)
        else:
            self.events.insert(pos, event)

