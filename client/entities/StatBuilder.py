def StatBuilderWeapon(MeleeDamage=0, SpellDamage=0, Health=100, AttackRange=1, FireDamage=0, ElectricDamage=0, Abilities=(None, None, None, None)):
    class result:
        meleeDamage = MeleeDamage
        spellDamage = SpellDamage
        health = Health
        attackRange = AttackRange

        # Status Damage Types
        fireDamage = FireDamage
        electricDamage = ElectricDamage

        abilities = Abilities

    return result

def StatBuilder(MeleeDamage=0, SpellDamage=0, Health=100):
    class result:
        meleeDamage = MeleeDamage
        spellDamage = SpellDamage
        health = Health

    return result