from client.guis.impl.GUIEnchantingMenu import GUIEnchantingMenu
from client.crafting.CraftingManager import craftingmanager
from client.crafting.impl.melee.Yoogi import Yoogi
from client.guis.impl.GUICraftingMenu import GUICraftingMenu
from pygame.constants import USEREVENT
from client.guis.impl.GUIDead import GUIDead
from client.guis.impl.GUISkillsMenu import GUISkillsMenu
from client.guis.GuiManager import GuiManager
from client.guis.impl.GUIIngame import GUIIngame
from client.guis.impl.GUICompletedGame import GUICompletedGame
from client.guis.impl.GUIEnterDungeon import GUIEnterDungeon
from client.guis.impl.GUIMainMenu import GUIMainMenu
from client.event.impl.MouseDownEvent import MouseDownEvent
from client.event.impl.KeydownEvent import KeydownEvent
from font.FontManager import FontManager
from client.event.impl.PlayerExitDungeonEvent import PlayerExitDungeonEvent
from client.rooms.RoomManager import roommanager
from client.entities.impl.Player import Player

# Rooms / Levels
from client.rooms.impl.tutorial import Tutorial
from client.rooms.impl.starGrove import StarGrove

import client.conf as conf

import pygame
from client.globals import globals

from client.conf import screenwidth, screenheight
from client.handlers.handleMovement import handleMovement

# Entities
from client.entities.impl.Player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((screenwidth, screenheight))

    print(conf.RESOURCE_DIR + "/entities/items/Oblivion.png")

    pygame.display.set_caption("RUMBATALE!")

    fontmanager = FontManager()
    guimanager = GuiManager()

    player = Player()

    player.setPos(screenwidth / 2 - (player.width / 2), screenheight / 2 - (player.height / 2))

    roommanager.rooms.append(Tutorial)
    roommanager.rooms.append(StarGrove)

    HALFSECOND = USEREVENT + 1

    pygame.time.set_timer(HALFSECOND, 500)

    Yoogi(craftingmanager)

    while globals.isRunning:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        if globals.hasStartedDungeon:
            p = player.getRect()
            exit = roommanager.currentRoom.getExit().getScreenRect()

            if p.colliderect(exit):
                PlayerExitDungeonEvent().child.call(player)

            handleMovement(player, keys, roommanager.currentRoom, guimanager)

        for event in events:
            if event.type == HALFSECOND:
                if player.mana < player.MaxMana:
                    player.mana += player.manaRegenAmount

                changeNumber = 0
                for timedChange in globals.timedChanges:

                    globals.timedChanges[changeNumber].time -= 0.5

                    if globals.timedChanges[changeNumber].time <= 0:
                        globals.timedChanges[changeNumber].revertPropertyChange()
                        del globals.timedChanges[changeNumber]
                    
                    changeNumber += 1

                buffNumber = 0
                for buff in globals.buffs:
                    globals.buffs[buffNumber][3] -= 0.5

                    if globals.buffs[buffNumber][3] <= 0:
                        setattr(player, buff[0], globals.buffs[buffNumber][1])
                        del globals.buffs[buffNumber]

                    buffNumber += 1

                enemyNumber = 0
                for enemy in globals.enemies:
                    globals.enemies[enemyNumber].shockTimer -= 0.5

                    if enemy.shockTimer <= 0:
                        enemy.shocked = False

                        globals.enemies[enemyNumber].shockTimer = 0

                    for statusEffect in enemy.statusEffects:
                        globals.enemies[enemyNumber].decreaseStatusEffectTime(statusEffect[2], 0.5)

                        if statusEffect[2] == "FireDamage":
                            dmg = (statusEffect[1].stats.fireDamage / 2)
                            globals.enemies[enemyNumber].health -= dmg

                            globals.enemies[enemyNumber].addLingeringDamageNumber(dmg)

                            if globals.enemies[enemyNumber].health <= 0:
                                del globals.enemies[enemyNumber]

                    for index in range(len(enemy.lingeringDamageNumbers)):
                        exists = len(globals.enemies) > enemyNumber and len(globals.enemies[enemyNumber].lingeringDamageNumbers) > index

                        if exists:
                            globals.enemies[enemyNumber].lingeringDamageNumbers[index][1] -= 0.5

                            if globals.enemies[enemyNumber].lingeringDamageNumbers[index][1] <= 0:
                                del globals.enemies[enemyNumber].lingeringDamageNumbers[index]


                    enemyNumber += 1
                
            if event.type == pygame.QUIT:
                globals.isRunning = False

            if event.type == pygame.KEYDOWN:
                KeydownEvent().child.call(event, player, guimanager)

            if event.type == pygame.MOUSEBUTTONDOWN:
                MouseDownEvent().child.call(event, player)

        screen.fill((0, 0, 0))

        if globals.hasStartedGame:
            if globals.hasStartedDungeon:
                if globals.hasCompletedDungeon == False:
                    if player.isDead:
                        guimanager.setGUI(GUIDead)
                    else:    
                        if globals.hasSkillsMenuOpen:
                            guimanager.setGUI(GUISkillsMenu)
                        elif globals.hasCraftingMenuOpen:
                            guimanager.setGUI(GUICraftingMenu)
                        elif globals.hasEnchantingMenuOpen:
                            guimanager.setGUI(GUIEnchantingMenu)

                        else:
                            guimanager.setGUI(GUIIngame)
                else:
                    guimanager.setGUI(GUICompletedGame)
            else:
                guimanager.setGUI(GUIEnterDungeon)
        else:
            guimanager.setGUI(GUIMainMenu)

        guimanager.drawGUI(screen, fontmanager, screenwidth, screenheight, player, guimanager)

        pygame.display.update()

main()