from client.items.weapons.Weapon import Weapon
from client.items.enchantments.Enchantment import EnchantingBook

class Inferno(EnchantingBook):
    def __init__(self, x, y):
        super().__init__("Inferno", [["fireDamage", 10]], [Weapon], (x, y))