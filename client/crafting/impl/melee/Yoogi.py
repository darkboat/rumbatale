from crafting.Craftable import Craftable


import items.weapons.impl.melee as weapons

class Yoogi(Craftable):
    def __init__(self, craftingmanager):
        super().__init__(weapons.Yoogi, [weapons.Scythe, weapons.RottenSword], craftingmanager)