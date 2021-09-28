from client.items.consumables.potions.StatBoostPotion import StatBoostPotion

class Invincibility(StatBoostPotion):
    def __init__(self, x, y):
        super().__init__("Invincibility", x, y)

    def onConsume(self, player):
        if not player.invincible:
            player.invincible = True

            super().addBuff("invincible", False, True, 5)

            super().onConsume(player)