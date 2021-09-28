from client.items.keys.Key import Key

class RedKey(Key):
    def __init__(self, x, y, canBePickedUp=False):
        super().__init__("Red_Key", x, y, False)

        self.canBePickedUp = canBePickedUp