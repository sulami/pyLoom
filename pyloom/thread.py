class Thread(object):
    """Subplot that holds story items"""

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

