from items.ItemManager import itemmanager
from rooms.RoomManager import roommanager

from globals import globals
import conf

import pygame

class GUIIngame:
    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        roommanager.drawRoom(screen, player, fontmanager)

        itemmanager.draw(screen)
        
        player.draw(screen, fontmanager)

        screen.blit(fontmanager.hudText.render("Dungeon Stage " + str(roommanager.roomNumber + 1), False, (255, 0, 0)), (10, 125))
        screen.blit(fontmanager.hudText.render("Dungeon " + roommanager.currentRoom.name, False, (255, 0, 0)), (10, 175))
        screen.blit(fontmanager.hudText.render(str(player.health) + "/" + str(player.MaxHealth) + "HP", False, (255, 0, 0)), (conf.screenwidth - 265, 10))
        screen.blit(fontmanager.hudText.render(str(player.mana) + "/" + str(player.MaxMana) + "MANA", False, (255, 0, 0)), (conf.screenwidth - 270, 55))