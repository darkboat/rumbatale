from client.entities.Entity import Entity

from client.globals import globals
import client.conf as conf

import pygame

class EntityLiving(Entity):
    def __init__(self, stats, pos, scale, speed, prev, cameraController, exit=globals.entities):
        super().__init__(pos, scale, speed, prev, cameraController, exit=exit)
        self.defaultMeleeDamage = stats.meleeDamage
        self.meleeDamage = stats.meleeDamage

        self.defaultSpellDamage = stats.spellDamage
        self.spellDamage = stats.spellDamage

        self.health = stats.health
        self.MaxHealth = stats.health