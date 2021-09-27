from items.keys.Key import Key
from rooms.impl.tutorial import Tutorial
from rooms.RoomManager import roommanager
from event.Event import Event

from items.keys.impl.red import RedKey

from globals import globals
import client_globals as cGlobals

class PlayerExitDungeonEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, player):
        if player.isHoldingItem(roommanager.currentRoom.exitKey):
            globals.entities = [x for x in globals.entities if x == player]

            player.removeItemReferencesFromInventory(roommanager.currentRoom.exitKey)
            
            cGlobals.cameraX = cGlobals.defaultCameraX
            cGlobals.cameraY = cGlobals.defaultCameraY
            player.miniMapX = 0
            player.miniMapY = 0

            next = roommanager.getNextRoom()

            if next == False:
                globals.hasCompletedDungeon = True

            else:
                globals.hasCompletedDungeon = False
                globals.hasStartedDungeon = True
                globals.hasStartedGame = True
                
                roommanager.setRoom(next)