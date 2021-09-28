from client.items.consumables.potions.StatBoostPotion import StatBoostPotion

class SpeedPotion(StatBoostPotion):
    def __init__(self, x, y):
        super().__init__("Speed+", x, y)

    def onConsume(self, player):
        speedmultiplier = 1.5

        player.speed *= speedmultiplier

        super().addBuff("speed", player.defaultSpeed, speedmultiplier, 60)

        super().onConsume(player)