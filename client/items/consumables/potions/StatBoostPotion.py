from client.items.consumables.potions.Potion import Potion

from client.globals import globals

class StatBoostPotion(Potion):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def addBuff(self, prop, default, multiplier, time):
        globals.buffs.append([prop, default, multiplier, time])

    def onConsume(self, player):
        return super().onConsume(player)