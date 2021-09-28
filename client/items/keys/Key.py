from client.entities.impl.Item import Item

class Key(Item):
    def __init__(self, name, x, y, canBePickedUp=True):
        super().__init__(name, (x, y), canBePickedUp)