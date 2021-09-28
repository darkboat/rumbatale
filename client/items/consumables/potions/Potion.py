from client.entities.impl.Consumable import Consumable


class Potion(Consumable):
    def __init__(self, name, x, y):
        super().__init__(name, (x, y))

    def onConsume(self, player):
        super().onConsume(player)