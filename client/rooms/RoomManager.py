from event.impl.ChangeRoomEvent import ChangeRoomEvent

from globals import globals

class RoomManager:
    def __init__(self):
        self.currentRoom = None
        self.roomNumber = 0
        self.rooms = []

    def drawRoom(self, screen, player, fontmanager):
        if self.currentRoom != None: 
            self.currentRoom.draw(screen, player, fontmanager)

    def setRoom(self, room):
        globals.entities = []
        globals.items = []
        globals.enemies = []

        ChangeRoomEvent().child.call(room)

        self.currentRoom = room()
        
        self.currentRoom.setStartingItems()
        
    def getNextRoom(self):
        next = (self.rooms[self.roomNumber + 1])

        self.roomNumber += 1

        return next

roommanager = RoomManager()