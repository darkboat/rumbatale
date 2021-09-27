from ui.MiniMap import MiniMap
from rooms.RoomManager import roommanager

from entities.impl.Tile import Tile

from math import ceil

from globals import globals
import conf

class Room:
    def __init__(self, walls, items, enemies, child, exitKey):
        self.walls = walls
        self.startingItems = items
        self.enemies = enemies
        self.child = child

        self.exitKey = exitKey

        self.setStartingItems()

    def setStartingItems(self):
        globals.items = self.startingItems.copy()
        globals.enemies = self.enemies.copy()

    def addWall(self, tile):
        self.walls.append(tile)

    def draw(self, screen, player, fontmanager):
        for wall in self.walls:
            wall.draw(screen)

        MiniMap.DrawMap(screen, player)

        for enemy in globals.enemies:
            enemy.Tick(player)

            if enemy.getIsOnScreen():
                enemy.draw(screen, fontmanager)

    def getRoomWidth(self):
        return self.getBottomWall().width

    def getRoomHeight(self):
        return self.getLeftWall().height

    def getLeftWall(self):
        return self.walls[0]

    def getRightWall(self):
        return self.walls[1]

    def getTopWall(self):
        return self.walls[2]

    def getBottomWall(self):
        return self.walls[3]

    def getExit(self):
        return self.walls[4]

    def update(self):
        roommanager.rooms[self.child.index] = self