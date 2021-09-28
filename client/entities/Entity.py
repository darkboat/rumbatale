import json
import pygame

from globals import globals
import conf

import client_globals as cGlobals

class Entity:
    def __init__(self, pos, scale, speed, prev, cameraController, exit=globals):
        self.exit = exit
        
        self.posX = pos[0]
        self.posY = pos[1]

        self.lastX = 0
        self.lastY = 0

        self.width = scale[0]
        self.height = scale[1]

        self.defaultWidth = self.width
        self.defaultHeight = self.height

        self.defaultSpeed = speed
        self.speed = speed

        self.color = None
        self.image = None
        self.downImage = None
        self.upImage = None

        self.cameraController = cameraController

        self.index = 0

        self.lastDirection = "right"

        if type(prev) == type(()):
            self.color = prev
        else:
            self.image = pygame.transform.smoothscale(prev, (self.width, self.height))

            print(conf.RESOURCE_DIR + "/entities/player/playerDown.png")
            
            self.downImage = pygame.transform.smoothscale(pygame.image.load(conf.RESOURCE_DIR + "/entities/player/playerDown.png").convert_alpha(), (self.width, self.height)).convert_alpha()
            self.upImage = pygame.transform.smoothscale(pygame.image.load(conf.RESOURCE_DIR + "/entities/player/playerUp.png").convert_alpha(), (self.width, self.height)).convert_alpha()

        self.scaledImage = self.image
        self.scaledUpImage = self.upImage
        self.scaledDownImage = self.downImage
        
    def flipImage(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def scaleImage(self):
        self.scaledImage = pygame.transform.smoothscale(self.image, (self.width, self.height))

    def scaleDownImage(self):
        self.scaledDownImage = pygame.transform.smoothscale(self.scaledDownImage, (self.width, self.height))

    def scaleUpImage(self):
        self.scaledUpImage = pygame.transform.smoothscale(self.scaledUpImage, (self.width, self.height))

    def setPos(self, x, y):
        self.posX = x
        self.posY = y

        self.update()

    def setPosX(self, x):
        self.posX = x
        
        self.update()
    
    def setPosY(self, y):
        self.posY = y

        self.update()

    def setLastPos(self, x, y):
        self.lastX = x
        self.lastY = y

        self.update()

    def setLastPosX(self, x):
        self.lastX = x

        self.update()

    def setLastPosY(self, y):
        self.lastY = y

        self.update()

    def setColor(self, color):
        self.color = color

        self.update()

    def update(self):
        pass
    
    def getRect(self):
        return pygame.Rect(self.posX, self.posY, self.width, self.height)
        
    def getScreenRect(self):
        returnVal = []

        if self.cameraController:
            returnVal.append(pygame.Rect(self.posX, self.posY, self.width, self.height))

        else:
            returnVal.append(pygame.Rect(self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY, self.width, self.height))
            
        return returnVal[0]

    def draw(self, screen):
        if self.color != None:
            pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.width, self.height)) if self.cameraController else pygame.draw.rect(screen, self.color, (self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY, self.width, self.height))
        else:
            if self.lastDirection == "up":
                image = self.upImage if self.width == self.defaultWidth and self.height == self.defaultHeight else self.scaledUpImage
                screen.blit(image, (self.posX, self.posY)) if self.cameraController else screen.blit(image, (self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY))

            if self.lastDirection == "down":
                image = self.downImage if self.width == self.defaultWidth and self.height == self.defaultHeight else self.scaledDownImage
                
                screen.blit(image, (self.posX, self.posY)) if self.cameraController else screen.blit(image, (self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY))

            if self.lastDirection == "left":
                image = self.image if self.width == self.defaultWidth and self.height == self.defaultHeight else self.scaledImage

                screen.blit(image if self.width == self.defaultWidth and self.height == self.defaultHeight else self.scaledImage, (self.posX, self.posY)) if self.cameraController else screen.blit(image, (self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY))

            if self.lastDirection == "right":
                image = self.image if self.width == self.defaultWidth and self.height == self.defaultHeight else self.scaledImage

                screen.blit(image if self.width == self.defaultWidth and self.height == self.defaultHeight else self.scaledImage, (self.posX, self.posY)) if self.cameraController else screen.blit(image, (self.posX - cGlobals.cameraX, self.posY - cGlobals.cameraY))

    def getIsOnScreen(self):
        x = self.posX - cGlobals.cameraX
        y = self.posY - cGlobals.cameraY
        w = self.width
        h = self.height

        return x + w > 0 and x < conf.screenwidth and y + h > 0 and y < conf.screenheight

    def toJSON(self, child):
        return json.dumps(child.__dict__)