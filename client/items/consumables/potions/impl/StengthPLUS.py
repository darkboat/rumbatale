from items.consumables.potions.StatBoostPotion import StatBoostPotion

class StrengthPotion(StatBoostPotion):
    def __init__(self, x, y):
        super().__init__("Strength+", x, y)

    def onConsume(self, player):
        damageMultiplier = 2

        player.meleeDamage *= damageMultiplier

        super().addBuff("meleeDamage", player.defaultMeleeDamage, damageMultiplier, 30)
        super().addBuff("spellDamage", player.defaultSpellDamage, damageMultiplier, 30)
        
        super().onConsume(player)