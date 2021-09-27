from conf import ROOT_DIR
import pygame

class FontManager:
    def __init__(self):
        fontdir = ROOT_DIR + "/font/fonts/"

        self.hudText = pygame.font.Font(fontdir + "Roboto-Black.ttf", 25)
        self.inventoryItemText = pygame.font.Font(fontdir + "Gluten-Thin.ttf", 20)
        self.titleText = pygame.font.Font(fontdir + "SigmarOne-Regular.ttf", 35)
        self.textInput = pygame.font.Font(fontdir + "Roboto-Black.ttf", 15)
        self.damageNumbers = pygame.font.Font(fontdir + "SigmarOne-Regular.ttf", 20)