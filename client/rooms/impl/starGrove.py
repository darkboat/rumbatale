from items.weapons.impl.melee.Yoogi import Yoogi
from enemies.Crawler import Crawler
from items.keys.impl.red import RedKey
from entities.impl.DungeonExit import DungeonExit
from rooms.Room import Room

import random

# Conf
import conf

# Entities
from entities.impl.Ref import Ref

class StarGrove(Room):
    def __init__(self):
        # Walls
        color = (13, 14, 13)

        dungeonWidth = conf.screenwidth * 5 + conf.borderWidth
        dungeonHeight = conf.screenheight * 5

        leftWall = Ref(0, 0, conf.borderWidth, dungeonHeight, color)
        rightWall = Ref((dungeonWidth + 1) / 50, 0, conf.borderWidth, dungeonHeight, color)
        topWall = Ref(0, 0, dungeonWidth, conf.borderWidth, color)
        bottomWall = Ref(0, dungeonHeight / 50, dungeonWidth, conf.borderWidth, color)
        dungeonExit = DungeonExit(int(conf.tilesPerColumn / 2), 1, 1, 1)

        # Keys
        redKey = RedKey(100, 100)

        # Enemies
        enemies = []

        for i in range(100):
            def getRandXAndY():
                randX = random.randrange(0, dungeonWidth - conf.tileSize)
                randY = random.randrange(0, dungeonHeight - conf.tileSize)

                isEnemyInLocation = any(e.posX == randX and e.posY == randY for e in enemies)

                return getRandXAndY() if isEnemyInLocation else randX, randY
            
            randX, randY = getRandXAndY()

            enemies.append(Crawler((randX, randY)))
            
        self.name = "Star Grove"
        super().__init__([leftWall, rightWall, topWall, bottomWall, dungeonExit], [redKey], enemies, self, RedKey)