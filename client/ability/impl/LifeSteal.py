from client.ability.Ability import Ability

from globals import globals
import client_globals as cGlobals
import conf

class LifeSteal(Ability):
    def __init__(self):
        super().__init__("LifeSteal", 25, self.onUse)

    def onUse(self, player):
        if player.health < player.MaxHealth + player.overHeal:
            heldItem = player.getHeldItem()

            gotHealth = False

            enemyNumber = 0
            for enemy in globals.enemies:
                tempDistance = abs((player.posX + cGlobals.cameraX - enemy.posX) + (player.posY + cGlobals.cameraY - enemy.posY))
                distanceFromPlayer = round(tempDistance/conf.tileSize)

                if distanceFromPlayer < 5:
                    lifeSteal = ((globals.enemies[enemyNumber].MaxHealth * (heldItem.stats.spellDamage if (heldItem.stats.spellDamage if hasattr(heldItem, "stats") else 0) > 0 else 1)) / 5)
                    globals.enemies[enemyNumber].health -= lifeSteal

                    if globals.enemies[enemyNumber].health <= 0:
                        del globals.enemies[enemyNumber]

                    player.health += lifeSteal
                    
                    gotHealth = True

                    print(lifeSteal)

                    if player.health > player.MaxHealth + player.overHeal:
                        player.health = player.MaxHealth + player.overHeal

                        break


                enemyNumber += 1

            if gotHealth:
                super().defaultFinish(player)

        else: return

        