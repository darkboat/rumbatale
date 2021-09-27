from event.Event import Event

class PlayerMoveEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, player):
        pass