from ability.impl.Reap import Reap
from ability.impl.Berserker import Berserker
from ability.impl.LifeSteal import LifeSteal
from ability.impl.Shock import Shock
from items.weapons.Weapon import Weapon

from entities.StatBuilder import StatBuilderWeapon

class Scythe(Weapon):
    def __init__(self, x, y):
        super().__init__("Scythe", StatBuilderWeapon(MeleeDamage=2.5, SpellDamage=0, Health=0, AttackRange=5, Abilities=(Shock, LifeSteal, Berserker, Reap)), (x, y))