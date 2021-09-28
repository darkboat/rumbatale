from client.entities.impl.Item import Item

class Consumable(Item):
    def __init__(self, item_name, pos):
        super().__init__(item_name, pos)

        self.cancelled = False

    def onConsume(self, player):
        if not self.cancelled:
            player.inventory[player.selectedInventorySlot] = None
        else:
            self.cancelled = False

    def setCancelled(self, val):
        self.cancelled = val