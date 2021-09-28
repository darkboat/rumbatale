from client.entities.Entity import Entity

import client.conf as conf

class DungeonExit(Entity):
    def __init__(self, x, y, tileWidth, tileHeight):
        super().__init__((x * conf.tileSize, y * conf.tileSize), (tileWidth * conf.tileSize, tileHeight * conf.tileSize), 1, (255, 255, 255), False)