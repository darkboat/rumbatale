from entities.impl.Consumable import Consumable

class HPPlus(Consumable):
    def __init__(self, x, y):
        super().__init__("HP+", (x, y))

        self.cancelled = False

    def onConsume(self, player):
        player.health += 20

        if player.health == player.MaxHealth:
            super().setCancelled(True)
            
        if player.health > player.MaxHealth:
            player.health = player.MaxHealth

        

        super().onConsume(player)