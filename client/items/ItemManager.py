from client.globals import globals

from client.rooms.RoomManager import roommanager

class ItemManager:
    @staticmethod
    def draw(screen):
        for item in globals.items:
            if isinstance(item, roommanager.currentRoom.exitKey):
                if globals.enemies.__len__() == 0:
                    item.canBePickedUp = True
                    item.draw(screen)

            else:
                item.draw(screen)


itemmanager = ItemManager