from entities.Entity import Entity

import conf

class Ref(Entity):
    def __init__(self, x, y, refWidth, refHeight, color):
        super().__init__((x * conf.tileSize, y * conf.tileSize), (refWidth, refHeight), 0, color, False)