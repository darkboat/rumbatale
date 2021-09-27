import pygame


import conf

class TextView:
    def __init__(self, screen, fontmanager, text, x, y):
        screen.blit(fontmanager.inventoryItemText.render(text, False, (255, 255, 255)), (x, y))