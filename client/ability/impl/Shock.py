from client.ability.Ability import Ability

from client.globals import globals
import client.client_globals as cGlobals
import client.conf as conf

class Shock(Ability):
    def __init__(self):
        super().__init__("Shock", 20, self.onUse)

    def onUse(self, player):
        heldItem = player.getHeldItem()

        enemyNumber = 0
        for enemy in globals.enemies:
            tempDistance = abs((player.posX + cGlobals.cameraX - enemy.posX) + (player.posY + cGlobals.cameraY - enemy.posY))
            distanceFromPlayer = round(tempDistance/conf.tileSize)

            if distanceFromPlayer < 6:
                globals.enemies[enemyNumber].shocked = True
                globals.enemies[enemyNumber].shockTimer = 5
                globals.enemies[enemyNumber].addStatusEffect([5, heldItem, "electricDamage", (0, 255, 232)])

            enemyNumber += 1

        super().defaultFinish(player)