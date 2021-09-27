from entities.impl.Item import Item

import globals

class EnchantingBook(Item):
    def __init__(self, name, stats, types, pos):
        self.stats = stats
        self.types = types

        super().__init__(name, pos)

    def enchantItem(self, child, item):
        correctType = False

        for type in self.types:
            if isinstance(item, type):
                correctType = True
                break

        if correctType:
            item.addEnchantment(child, self.stats)