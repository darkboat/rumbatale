from client.rooms.RoomManager import roommanager

import client.conf as conf

import pygame

class MiniMap:
    @staticmethod
    def DrawMap(screen, player):
        mapSize = 100

        prx = player.miniMapX + conf.screenwidth - mapSize
        pry = player.miniMapY

        exit = roommanager.currentRoom.walls[4]

        pygame.draw.rect(screen, (0, 0, 50), (conf.screenwidth - mapSize, 0, mapSize, mapSize))
        pygame.draw.rect(screen, (255, 255, 255), (prx, pry, 2, 2))
        pygame.draw.rect(screen, (255, 0, 0), (((exit.posX + player.width) / mapSize) + (conf.screenwidth - mapSize) + 9, exit.posY / mapSize, 5, 5))