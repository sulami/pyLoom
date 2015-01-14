from pyloom.session import Session

class Campaign(object):
    """Holds all events in a given campaign"""

    def __init__(self, name):
        self.name = name
        self.sessions = []

    def add_session(self, session, pos=-1):
        s = Session(session)
        if pos == -1:
            self.sessions.append(s)
        else:
            self.sessions.insert(pos, s)

