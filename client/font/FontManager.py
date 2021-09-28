from conf import FONT_DIR
import pygame

class FontManager:
    def __init__(self):
        self.hudText = pygame.font.Font("C:/Users/mikae/AppData/Roaming/.rumbatale/client/font/fonts/Roboto-Black.ttf", 25)
        self.inventoryItemText = pygame.font.Font("C:/Users/mikae/AppData/Roaming/.rumbatale/client/font/fonts/Gluten-Thin.ttf", 20)
        self.titleText = pygame.font.Font("C:/Users/mikae/AppData/Roaming/.rumbatale/client/font/fonts/SigmarOne-Regular.ttf", 35)
        self.textInput = pygame.font.Font("C:/Users/mikae/AppData/Roaming/.rumbatale/client/font/fonts/Roboto-Black.ttf", 15)
        self.damageNumbers = pygame.font.Font("C:/Users/mikae/AppData/Roaming/.rumbatale/client/font/fonts/SigmarOne-Regular.ttf", 20)