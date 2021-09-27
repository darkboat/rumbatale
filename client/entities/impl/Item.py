import pygame

from globals import globals
import conf

from entities.Entity import Entity

class Item(Entity):
    def __init__(self, item_name, pos, canBePickedUp=True, loc=globals.items):
        self.name = item_name
        self.pos = pos

        self.canBePickedUp = canBePickedUp

        image = pygame.image.load(conf.ROOT_DIR.replace("\\", "/") + "/resources/entities/items/" + item_name + ".png").convert_alpha()

        super().__init__(pos, (50, 50), 0.25, image, False, loc)