class EventManager:
    def __init__(self):
        self.events = []

    def subscribe(self, event):
        self.events.append(event)

eventmanager = EventManager()