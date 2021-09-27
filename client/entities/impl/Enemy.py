from entities.EntityLiving import EntityLiving
import pygame

import client_globals as cGlobals

from globals import globals
import conf

import random

class Enemy(EntityLiving):
    def __init__(self, stats, enemy_name, pos, speed, loc=globals.enemies):
        self.name = enemy_name
        self.pos = pos

        self.dropTable = []

        self.statusEffects = []

        self.lingeringDamageNumbers = []

        self.shocked = False
        self.shockTimer = 0

        image = pygame.image.load(conf.ROOT_DIR.replace("\\", "/") + "/resources/entities/enemies/" + enemy_name + ".png").convert_alpha()

        super().__init__(stats, pos, (50, 50), speed, image, False, loc)

    def initDropTable(self, drops):
        for drop in drops:
            chance, item = drop

            for _ in range(chance):
                self.dropTable.append(item)

        if len(self.dropTable) < 10000:
            toAdd = 10000 - len(self.dropTable)

            for i in range(toAdd):
                self.dropTable.append(None)

    def spawnRandomDrop(self, x, y):
        drop = self.dropTable[random.randrange(0, 10000)]

        if drop != None:
            globals.items.append(drop(x, y))

    def addLingeringDamageNumber(self, damage, time=2):
        self.lingeringDamageNumbers.append([damage, time, (0, random.randrange(0, self.height))])

    def addStatusEffect(self, statusEffect):
        self.statusEffects.append(statusEffect)

    def removeStatusEffect(self, statusEffectName):
        found = None

        i = 0
        for statusEffect in self.statusEffects:
            if statusEffect[2] == statusEffectName:
                found = i

            i += 1

        if found != None:
            del self.statusEffects[found]

    # STATUS STRUCTURE [time, starter, name, color]

    def getStatusEffect(self, statusEffectName):
        found = None

        for statusEffect in self.statusEffects:
            if statusEffect[2] == statusEffectName:
                found = statusEffect

        return found

    def getStatusEffectIndex(self, statusEffectName):
        found = -1

        i = 0
        for statusEffect in self.statusEffects:
            if statusEffect[2] == statusEffectName:
                found = i

            i += 1

        return found

    def increaseStatusEffectTime(self, statusEffectName, increaseAmount):
        index = self.getStatusEffectIndex(statusEffectName)

        self.statusEffects[index][0] += increaseAmount

    def decreaseStatusEffectTime(self, statusEffectName, decreaseAmount):
        index = self.getStatusEffectIndex(statusEffectName)

        if index > -1:
            if len(self.statusEffects) > index:
                if (len(self.statusEffects[index]) if len(self.statusEffects) > index else 0) > 0:
                    self.statusEffects[index][0] -= decreaseAmount

            if self.statusEffects[index][0] <= 0:
                del self.statusEffects[index]

    def draw(self, screen, fontmanager):
        super().draw(screen)
        self.drawStatusEffects(screen)
        self.drawLingeringDamageNumbers(screen, fontmanager)

    def drawStatusEffects(self, screen):
        for statusEffect in self.statusEffects:
            if statusEffect[0] > 0:
                for i in range(1):
                    randX = random.randrange(0, self.width)
                    randY = random.randrange(0, self.height)

                    pygame.draw.rect(screen, (statusEffect[3][0], statusEffect[3][1], statusEffect[3][2]), (self.posX - cGlobals.cameraX + randX, self.posY - cGlobals.cameraY + randY, 2, 2))

    def enflictStatus(self, heldItem):
        if heldItem == None: return

        if heldItem.stats.fireDamage > 0:
            index = self.getStatusEffectIndex("FireDamage")

            if index == -1:
                self.addStatusEffect([5, heldItem, "FireDamage", (255, 128, 80)])
            else:
                self.increaseStatusEffectTime("FireDamage", 5)

        if heldItem.stats.electricDamage > 0:
            index = self.getStatusEffectIndex("ElectricDamage")

            if index == -1:
                self.addStatusEffect([5, heldItem, "ElectricDamage", (0, 255, 232)])
            else:
                self.increaseStatusEffectTime("ElectricDamage", 5)

    def drawLingeringDamageNumbers(self, screen, fontmanager):
        for ldn in self.lingeringDamageNumbers:
            screen.blit(fontmanager.damageNumbers.render("-" + str(ldn[0]), False, (255, 0, 0)), (self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY - 20 + ldn[2][1]))