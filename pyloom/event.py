class Event(object):
    """An entry in the log"""

    def __init__(self, session):
        self.session = session
        self.session.events.append(self)

