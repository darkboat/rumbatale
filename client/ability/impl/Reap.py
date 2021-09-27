from ability.Ability import Ability

from globals import globals
import client_globals as cGlobals
import conf

class Reap(Ability):
    def __init__(self):
        super().__init__("Reap", 100, self.onUse)

    def onUse(self, player):
        REAPDAMAGE = 750

        enemyNumber = 0
        for enemy in globals.enemies:
            tempDistance = abs((player.posX + cGlobals.cameraX - enemy.posX) + (player.posY + cGlobals.cameraY - enemy.posY))
            distanceFromPlayer = round(tempDistance/conf.tileSize)

            if distanceFromPlayer < 5:
                globals.enemies[enemyNumber].health -= REAPDAMAGE
                
                if globals.enemies[enemyNumber].health <= 0:
                    del globals.enemies[enemyNumber]


            enemyNumber += 1

        super().defaultFinish(player)
