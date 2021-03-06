from client.items.consumables.potions.impl.Invincibility import Invincibility
from client.items.consumables.potions.impl.StengthPLUS import StrengthPotion
from client.items.weapons.impl.melee.Scythe import Scythe
from client.enemies.Crawler import Crawler
from client.items.keys.impl.red import RedKey
from client.entities.impl.DungeonExit import DungeonExit
from client.rooms.Room import Room
from client.items.enchantments.impl.Inferno import Inferno

# Conf
import client.conf as conf

# Entities
from client.entities.impl.Ref import Ref

from client.items.consumables.potions.impl.HPPLUS import HPPlus
from client.items.consumables.potions.impl.SpeedPLUS import SpeedPotion

class Tutorial(Room):

    def __init__(self):
        # Walls
        color = (13, 14, 13)

        dungeonWidth = conf.screenwidth * 3 + conf.borderWidth
        dungeonHeight = conf.screenheight * 3

        leftWall = Ref(0, 0, conf.borderWidth, dungeonHeight, color)
        rightWall = Ref((dungeonWidth + 1) / 50, 0, conf.borderWidth, dungeonHeight, color)
        topWall = Ref(0, 0, dungeonWidth, conf.borderWidth, color)
        bottomWall = Ref(0, dungeonHeight / 50, dungeonWidth, conf.borderWidth, color)
        dungeonExit = DungeonExit(int(conf.tilesPerColumn / 2), 1, 1, 1)

        # Enemies
        crawler1 = Crawler((600, 400))

        # Keys
        redkey =  RedKey(int(conf.tilesPerColumn / 2) * conf.tileSize, 50)

        # Items (On Ground)
        scythe = Scythe(150, 100)

        inferno = Inferno(200, 200)

        invincibility = Invincibility(250, 200)
        strengthplus = StrengthPotion(300, 200)
        hpplus = HPPlus(350, 200)
        speedplus = SpeedPotion(400, 200)
        
        self.name = "tutorial"
        super().__init__([leftWall, rightWall, topWall, bottomWall, dungeonExit], [redkey, scythe, inferno, invincibility, strengthplus, hpplus, speedplus], [crawler1], self, RedKey)