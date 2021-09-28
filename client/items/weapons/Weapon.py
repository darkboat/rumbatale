from client.entities.impl.Item import Item

from globals import globals

class Weapon(Item):
    def __init__(self, name, stats, pos):
        self.stats = stats
        self.enchantments = []

        super().__init__(name, pos)

    def addEnchantment(self, enchantment, stats):
        for stat in stats:
            setattr(self.stats, stat[0], getattr(self.stats, stat[0]) + stat[1])
            self.enchantments.append(type(enchantment).__name__)