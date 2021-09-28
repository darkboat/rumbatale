from client.event.Event import Event

class ChangeRoomEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, room):
        pass