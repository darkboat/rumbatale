import os

screenwidth = 800
screenheight = 800

tileSize = 50

tilesPerRow = screenwidth / tileSize
tilesPerColumn = screenheight / tileSize

inventoryLength = 5

borderWidth = 5

inventoryBoxColor = (117, 117, 117)
inventoryBoxSelectedColor = (205, 205, 205)
textInputSelectedOutline = (184, 184, 184)

APPDATA = os.getenv("APPDATA")
GAME_DIR = str(APPDATA) + "/.rumbatale/client"

RESOURCE_DIR = GAME_DIR + "/resources"
FONT_DIR = GAME_DIR + "/font/fonts"