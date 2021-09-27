from items.weapons.Weapon import Weapon

from entities.StatBuilder import StatBuilderWeapon

class Yoogi(Weapon):
    def __init__(self, x, y):
        super().__init__("Yoogi", StatBuilderWeapon(MeleeDamage=15, SpellDamage=5, Health=0, AttackRange=2), (x, y))