from ability.TimedPropertyChange import TimedPropertyChange
from ability.Ability import Ability

class Berserker(Ability):
    def __init__(self, ):
        super().__init__("Berserker", 50, self.onUse)

    def onUse(self, player):
        heldItem = player.getHeldItem()

        if not player.isBerserk:
            TimedPropertyChange(heldItem, ["stats", "meleeDamage"], (heldItem.stats.meleeDamage if hasattr(heldItem, "stats") else 0) * 2, 10)

            super().defaultFinish(player)