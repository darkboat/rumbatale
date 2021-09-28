from conf import FONT_DIR
import pygame

class FontManager:
    def __init__(self):
        self.hudText = pygame.font.Font(FONT_DIR + "Roboto-Black.ttf", 25)
        self.inventoryItemText = pygame.font.Font(FONT_DIR + "Gluten-Thin.ttf", 20)
        self.titleText = pygame.font.Font(FONT_DIR + "SigmarOne-Regular.ttf", 35)
        self.textInput = pygame.font.Font(FONT_DIR + "Roboto-Black.ttf", 15)
        self.damageNumbers = pygame.font.Font(FONT_DIR + "SigmarOne-Regular.ttf", 20)