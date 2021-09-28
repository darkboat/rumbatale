from client.event.EventManager import eventmanager

class Event:
    def __init__(self, child):
        self.child = child

        eventmanager.subscribe(child)

    def call(self, *args):
        for event in eventmanager.events:
            if event == self.child:
                self.child.call(*args)