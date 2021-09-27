from event.impl.CurrentInventorySlotChangeEvent import CurrentInventorySlotChangeEvent
from ui.TextView import TextView
from items.keys.impl.red import RedKey
from entities.impl.Item import Item
from skills.SkillsManager import skillsmanager
from event.impl.PlayerKillEntityEvent import PlayerKillEntityEvent
from items.weapons.Weapon import Weapon
from entities.StatBuilder import StatBuilder
from entities.EntityLiving import EntityLiving

import client_globals as cGlobals

import pygame
from random import randrange

from globals import globals
import conf

class Player(EntityLiving):
    def __init__(self):
        self.image = pygame.image.load(conf.RESOURCE_DIR + "/entities/player/player.png")

        self.inventory = []

        self.selectedInventorySlot = 0

        self.showTrails = False

        self.isDead = False

        self.movingDirection = ""

        self.trailStaggerLeft = 3
        self.trailStaggerMiddle = 5
        self.trailStaggerRight = 1

        self.miniMapX = 0
        self.miniMapY = 0

        self.ability1 = None
        self.ability2 = None
        self.ability3 = None
        self.ability4 = None
        
        self.imageFlipped = False

        self.exp = 0

        self.mana = 100
        self.MaxMana = 100

        self.overHeal = 50

        self.manaRegenAmount = 5

        self.invincible = False
        self.isBerserk = False

        for i in range(conf.inventoryLength):
            self.inventory.append(None)

        super().__init__(StatBuilder(MeleeDamage=5, Health=125), pos=(0, 0), scale=(75, 150), speed=0.25, prev=self.image, cameraController=True, exit=globals.player)


        self.scaledImage = self.image

    def attack(self):
        p = self.getRect()

        heldItem = self.getHeldItem()

        rangeOfAttack = heldItem.stats.attackRange * conf.tileSize if isinstance(heldItem, Weapon) else 0

        p.x -= rangeOfAttack
        p.y -= rangeOfAttack
        p.width += rangeOfAttack * 2
        p.height += rangeOfAttack * 2

        enemyNumber = 0

        totalDamage = self.meleeDamage + (heldItem.stats.meleeDamage if isinstance(heldItem, Weapon) else 0)

        multiplier = 1

        i = 0
        for _ in range(skillsmanager.getSkill("Sharpifier").bar.level):
            multiplier += i / 2 if i > 0 else 0

            i += 1

        totalDamage *= multiplier

        for enemy in globals.enemies:
            e = enemy.getScreenRect()

            if p.colliderect(e):
                globals.enemies[enemyNumber].health -= totalDamage

                globals.enemies[enemyNumber].addLingeringDamageNumber(totalDamage)

                globals.enemies[enemyNumber].enflictStatus(heldItem)

                if enemy.health <= 0:

                    if len(globals.enemies) == 1:
                        RedKey(enemy.posX, enemy.posY, True)
                        
                    PlayerKillEntityEvent().child.call(enemy, self)

                    del globals.enemies[enemyNumber]

            enemyNumber += 1

    def getHeldItem(self):
        return self.inventory[self.selectedInventorySlot]

    def getHeldItemIndex(self):
        return self.selectedInventorySlot
    
    def isHoldingItem(self, item):
        return isinstance(self.inventory[self.selectedInventorySlot], item)

    def addItemToNextFreeSlot(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == None:
                self.inventory[i] = item

                break

    def addItemToInventory(self, item):
        if self.inventory[self.selectedInventorySlot] == None:
            self.inventory[self.selectedInventorySlot] = item
        else:
            old = self.inventory[self.selectedInventorySlot]

            old.posX = self.posX + cGlobals.cameraX
            old.posY = self.posY + cGlobals.cameraY

            globals.items.append(old)

            self.inventory[self.selectedInventorySlot] = item

        CurrentInventorySlotChangeEvent().child.call(self)

    def hasItemInInventory(self, item):
        hasItem = any(isinstance(x, item) for x in self.inventory)

        return hasItem

    def removeItemReferencesFromInventory(self, item):
        indexes = []

        i = 0
        for s in self.inventory:
            if isinstance(s, item):
                indexes.append(i)

            i += 1

        for index in indexes:
            self.inventory[index] = None

    def dropHeldItem(self):
        item = self.inventory[self.selectedInventorySlot]

        if item == None: return

        item.posX = self.posX + cGlobals.cameraX
        item.posY = self.posY + cGlobals.cameraY

        globals.items.append(item)

        self.inventory[self.selectedInventorySlot] = None

    def draw(self, screen, fontrenderer):
        self.drawInventory(screen, fontrenderer)

        if self.showTrails:
            self.drawTrailEffects(screen)

        if self.invincible:
            thickness = 5

            pygame.draw.rect(screen, (180, 253, 255), (int(self.posX - thickness), int(self.posY - thickness), self.width + thickness, thickness))
            pygame.draw.rect(screen, (180, 253, 255), (int(self.posX - thickness), int(self.posY - thickness), thickness, self.height + thickness))
            pygame.draw.rect(screen, (180, 253, 255), (int(self.posX + self.width), int(self.posY - thickness), thickness, self.height + thickness))
            pygame.draw.rect(screen, (180, 253, 255), (int(self.posX - thickness), int(self.posY + self.height), self.width + thickness + thickness, thickness))

        super().draw(screen)

    def drawInventory(self, screen, fontrenderer):
        def drawBoxOutline(x, y, w, h, outlineWidth, isSelected):
            col = conf.inventoryBoxColor if not isSelected else conf.inventoryBoxSelectedColor

            pygame.draw.rect(screen, col, (x, y, w, outlineWidth)) # Top
            pygame.draw.rect(screen, col, (x, y, outlineWidth, h)) # Left
            pygame.draw.rect(screen, col, (x, h, w + 2, outlineWidth)) # Bottom
            pygame.draw.rect(screen, col, (x + w, y, outlineWidth, h)) # Right

        def floorToInvThumbnail(thumbnail):
            return pygame.transform.smoothscale(thumbnail, (75, 75))

        mouseX, mouseY = pygame.mouse.get_pos()

        mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)

        for i in range(conf.inventoryLength):
            item = self.inventory[i]

            x = 0 + (i * 100)
            y = 0
            w = 100
            h = 100
            outlineWidth = 2

            drawBoxOutline(x, y, w, h, outlineWidth, False)

            if item != None:
                thumbnailX = x + 10
                thumnailY = y + 15

                screen.blit(floorToInvThumbnail(item.image), (thumbnailX, thumnailY))

                boxRect = pygame.Rect(x, y, w, h)

                if boxRect.colliderect(mouseRect):
                    TextView(screen, fontrenderer, item.name, 10, conf.screenheight - 25)

                    if item != None and hasattr(item, "enchantments"):
                        y = 0
                        for enchantment in item.enchantments:
                            TextView(screen, fontrenderer, enchantment, 5, 250 + (y * 50))

                            y += 1

            item = self.inventory[self.selectedInventorySlot]

            x = 0 + (self.selectedInventorySlot * 100)
            y = 0
            w = 100
            h = 100
            outlineWidth = 2

            drawBoxOutline(x, y, w, h, outlineWidth, True)
        
    def drawTrailEffects(self, screen):
        trailWidth = 5
        trailHeight = 40
        trailGapY = self.height + 10
        trailGapX = self.width + 10

        self.trailStaggerLeft = randrange(0, 2)
        self.trailStaggerMiddle = randrange(0, 5)
        self.trailStaggerRight = randrange(0, 3)

        extraGapY = self.height / 2
        extraGapUp = 20
        lessGapRight = 20

        if self.movingDirection == "up":
            leftTrail = pygame.Rect(self.posX, self.posY + trailGapY + self.trailStaggerLeft + extraGapUp, trailWidth, trailHeight)
            middleTrail = pygame.Rect(self.posX + (self.width / 2) - (trailWidth / 2) + 1, self.posY + trailGapY + self.trailStaggerMiddle + extraGapUp, trailWidth, trailHeight)
            rightTrail = pygame.Rect(self.posX + self.width - trailWidth, self.posY + trailGapY + self.trailStaggerRight + extraGapUp, trailWidth, trailHeight)

            pygame.draw.rect(screen, (255, 255, 255), leftTrail)
            pygame.draw.rect(screen, (255, 255, 255), middleTrail)
            pygame.draw.rect(screen, (255, 255, 255), rightTrail)

        if self.movingDirection == "down":
            leftTrail = pygame.Rect(self.posX, self.posY - trailGapY - self.trailStaggerLeft + extraGapY, trailWidth, trailHeight)
            middleTrail = pygame.Rect(self.posX + (self.width / 2) - (trailWidth / 2) + 1, self.posY - trailGapY - self.trailStaggerMiddle + extraGapY, trailWidth, trailHeight)
            rightTrail = pygame.Rect(self.posX + self.width - trailWidth, self.posY - trailGapY - self.trailStaggerRight + extraGapY, trailWidth, trailHeight)

            pygame.draw.rect(screen, (255, 255, 255), leftTrail)
            pygame.draw.rect(screen, (255, 255, 255), middleTrail)
            pygame.draw.rect(screen, (255, 255, 255), rightTrail)

        if self.movingDirection == "left":
            leftTrail = pygame.Rect(self.posX + trailGapX + self.trailStaggerLeft, self.posY, trailHeight, trailWidth)
            middleTrail = pygame.Rect(self.posX + self.trailStaggerMiddle + trailGapX, self.posY + (self.width / 2) - (trailWidth / 2), trailHeight, trailWidth)
            rightTrail = pygame.Rect(self.posX + trailWidth + trailGapX + self.trailStaggerRight, self.posY + self.width - trailWidth, trailHeight, trailWidth)

            pygame.draw.rect(screen, (255, 255, 255), leftTrail)
            pygame.draw.rect(screen, (255, 255, 255), middleTrail)
            pygame.draw.rect(screen, (255, 255, 255), rightTrail)

        if self.movingDirection == "right":
            leftTrail = pygame.Rect(self.posX - trailGapX - self.trailStaggerLeft + lessGapRight, self.posY, trailHeight, trailWidth)
            middleTrail = pygame.Rect(self.posX - self.trailStaggerMiddle - trailGapX + lessGapRight, self.posY + (self.width / 2) - (trailWidth / 2), trailHeight, trailWidth)
            rightTrail = pygame.Rect(self.posX - trailWidth - trailGapX - self.trailStaggerRight + lessGapRight, self.posY + self.width - trailWidth, trailHeight, trailWidth)

            pygame.draw.rect(screen, (255, 255, 255), leftTrail)
            pygame.draw.rect(screen, (255, 255, 255), middleTrail)
            pygame.draw.rect(screen, (255, 255, 255), rightTrail)

    def toJSON(self):
        return str(self.__dict__).replace("'", '"').replace("True", 'true').replace("False", "false").replace("None", "null")