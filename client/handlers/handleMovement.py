from client.entities.impl.Player import Player
from client.event.impl.PlayerMoveEvent import PlayerMoveEvent
import client.bindings as bindings
import client.conf as conf

from client.guis.impl.GUIIngame import GUIIngame

import client.client_globals as cGlobals


def handleMovement(entity, keys, room, guimanager):
    if not guimanager.currentGUI is GUIIngame: return

    entity.setLastPosX(entity.posX)
    entity.setLastPosY(entity.posY)

    leftWallX = room.getLeftWall().posX - cGlobals.cameraX
    rightWallX = room.getRightWall().posX - cGlobals.cameraX - conf.tileSize
    topWallY = room.getTopWall().posY - cGlobals.cameraY
    bottomWallY = room.getBottomWall().posY - cGlobals.cameraY - conf.tileSize

    hasMoved = []

    if keys[bindings.moveUp]:
        newX = entity.posX
        newY = entity.posY - entity.speed

        if newX > leftWallX and newX < rightWallX and newY < bottomWallY and newY > topWallY + conf.borderWidth:
            cGlobals.cameraY -= entity.speed if entity.cameraController else entity.setPosY(entity.posY - entity.speed)

            PlayerMoveEvent().child.call(entity)
            entity.miniMapY -= entity.speed / (room.getRoomHeight() / 100)
            entity.showTrails = True
            entity.movingDirection = "up"
            hasMoved.append(True)

            entity.lastDirection = "up"


    if keys[bindings.moveDown]:
        newX = entity.posX
        newY = entity.posY + entity.speed

        if newX > leftWallX and newX < rightWallX and newY < bottomWallY and newY > topWallY:
            cGlobals.cameraY += entity.speed if entity.cameraController else entity.setPosY(entity.posY + entity.speed)

            PlayerMoveEvent().child.call(entity)
            entity.miniMapY += entity.speed / (room.getRoomHeight() / 100)
            entity.showTrails = True
            entity.movingDirection = "down"
            hasMoved.append(True)

            entity.lastDirection = "down"

    if keys[bindings.moveLeft]:
        newX = entity.posX - entity.speed
        newY = entity.posY

        if newX > leftWallX + conf.borderWidth and newX < rightWallX and newY < bottomWallY and newY > topWallY:
            cGlobals.cameraX -= entity.speed if entity.cameraController else entity.setPosX(entity.posX - entity.speed)
            
            PlayerMoveEvent().child.call(entity)
            entity.miniMapX -= entity.speed / (room.getRoomWidth() / 100)
            entity.showTrails = True
            entity.movingDirection = "left"
            hasMoved.append(True)

            if not entity.imageFlipped:
                entity.flipImage()

                entity.imageFlipped = True

            entity.lastDirection = "left"

    if keys[bindings.moveRight]:
        newX = entity.posX + entity.speed
        newY = entity.posY

        if newX > leftWallX and newX < rightWallX and newY < bottomWallY and newY > topWallY:
            cGlobals.cameraX += entity.speed if entity.cameraController else entity.setPosY(entity.posX + entity.speed)

            PlayerMoveEvent().child.call(entity)
            entity.miniMapX += entity.speed / (room.getRoomWidth() / 100)
            entity.showTrails = True
            entity.movingDirection = "right"
            hasMoved.append(True)

            if entity.imageFlipped:
                entity.flipImage()

                entity.imageFlipped = False

            entity.lastDirection = "right"

    if not True in hasMoved:
        entity.showTrails = False
        entity.movingDirection = ""