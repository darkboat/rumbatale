import pygame

from client.entities.Entity import Entity

import client.conf as conf

class Tile(Entity):
    def __init__(self, x, y, tileWidth, tileHeight, name):
        path = conf.RESOURCE_DIR + "/static/tiles/" + name + ".png"

        super().__init__((x * conf.tileSize, y * conf.tileSize), (tileWidth * conf.tileSize, tileHeight * conf.tileSize), 1, pygame.image.load(path).convert_alpha(), False, [])