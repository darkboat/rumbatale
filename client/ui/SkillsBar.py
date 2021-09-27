from ui.Button import Button
import pygame

import conf

from globals import globals

class SkillsBar:
    def __init__(self, name, max, firstUpgradePrice):
        self.name = name
        self.level = 1
        self.MaxLevel = max

        self.upgradePrice = firstUpgradePrice

    def buyUpgrade(self, player):
        if self.level + 1 <= self.MaxLevel:
            price = self.getUpgradePrice()

            if player.exp >= price:
                self.level += 1

                player.exp -= price

    def getUpgradePrice(self):
        return self.level * (self.upgradePrice * 5)

    def getUpgradePriceForLevel(self, level):
        return level * (self.upgradePrice * 5)

    def draw(self, screen, fontmanager, startingX, y, guimanager):
        sectorSizeX = 25
        sectorSizeY = 50

        totalX = startingX

        def drawBoxOutline(x, y, w, h, outlineWidth):
            white = (255, 255, 255)

            pygame.draw.rect(screen, white, (x, y, w, outlineWidth)) # Top
            pygame.draw.rect(screen, white, (x, y, outlineWidth, h)) # Left
            pygame.draw.rect(screen, white, (x, y + h, w + 2, outlineWidth)) # Bottom
            pygame.draw.rect(screen, white, (x + w, y, outlineWidth, h)) # Right

            return w

        screen.blit(fontmanager.hudText.render("exp" + str(self.getUpgradePrice()) if self.level + 1 < self.MaxLevel else "MAX", False, (0, 255, 0)), (startingX - 35, y))
        screen.blit(fontmanager.hudText.render(self.name, False, (0, 255, 0)), (startingX + 75, y))

        paddingRight = 200

        totalX += paddingRight

        for x in range(self.MaxLevel):
            totalX += drawBoxOutline(startingX + paddingRight + (sectorSizeX * x), y - 10, sectorSizeX, sectorSizeY, 2)

        for x in range(self.level):
            pygame.draw.rect(screen, (14, 200, 56 ), (startingX + paddingRight + (sectorSizeX * x) + 2, y - 10 + 2, sectorSizeX - 2, sectorSizeY - 2))

        paddingRight = 25

        totalX += paddingRight

        btn = Button(fontmanager, totalX, y, 50, 50, "+")
        btn.setOnClickListener(lambda mouse: self.buyUpgrade(globals.player[0]))
        btn.draw(screen)