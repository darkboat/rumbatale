from client.items.weapons.Weapon import Weapon

from client.entities.StatBuilder import StatBuilderWeapon

class RottenSword(Weapon):
    def __init__(self, x, y):
        super().__init__("RottenSword", StatBuilderWeapon(10, 0, 0, 3), (x, y))