from event.impl.CurrentInventorySlotChangeEvent import CurrentInventorySlotChangeEvent
from guis.impl.GUIIngame import GUIIngame
import pygame
from entities.impl.Consumable import Consumable
from rooms.impl.tutorial import Tutorial
from rooms.RoomManager import roommanager
from event.Event import Event

import bindings
from globals import globals

class KeydownEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, event, player, guimanager):
        if event.key == pygame.K_ESCAPE:
            globals.hasSkillsMenuOpen = False
            globals.hasCraftingMenuOpen = False
            globals.hasEnchantingMenuOpen = False

        for textInput in globals.textinputs:
            textInput.onType(event)

        def getSlotBindings():
            slotBindings = []

            for bind in dir(bindings):
                if "slot" in bind:
                    slotNumber = int(bind.replace("slot", ""))
                    slotBindings.append([bind, slotNumber])

            return slotBindings
        if globals.hasStartedGame:
            if globals.hasStartedDungeon:
                if globals.hasCompletedDungeon:
                    globals.hasCompletedDungeon = False
                    globals.hasStartedDungeon = False

                else:
                    if player.isDead:
                        player.isDead = False
                        globals.hasSkillsMenuOpen = False
                        globals.hasEnchantingMenuOpen = False
                        globals.hasCraftingMenuOpen = False
                        globals.hasStartedDungeon = False
                        globals.hasStartedGame = False

                    if guimanager.currentGUI is GUIIngame:
                        # Abilities
                        if player.ability1 != None and event.key == bindings.ability1:
                            player.ability1().run(player)

                        if player.ability2 != None and event.key == bindings.ability2:
                            player.ability2().run(player)
                        
                        if player.ability3 != None and event.key == bindings.ability3:
                            player.ability3().run(player)

                        if player.ability4 != None and event.key == bindings.ability4:
                            player.ability4().run(player)


                        if event.key == bindings.consumeItem:
                            if player.isHoldingItem(Consumable):
                                player.inventory[player.selectedInventorySlot].onConsume(player)

                        if event.key == bindings.skillsMenu:
                            globals.hasSkillsMenuOpen = True

                        if event.key == bindings.craftingMenu:
                            globals.hasCraftingMenuOpen = True

                        if event.key == bindings.enchantingMenu:
                            globals.hasEnchantingMenuOpen = True
                            
                        if event.key == bindings.dropItem:
                            player.dropHeldItem()

                        if event.key == bindings.useItem:
                            collidingItemsIndexes = []
                            collidingItems = []

                            p = player.getRect()

                            index = 0
                            for item in globals.items:
                                if item.canBePickedUp:

                                    i = item.getScreenRect()

                                    if p.colliderect(i):
                                        collidingItems.append(item)
                                        collidingItemsIndexes.append(index)

                                index += 1

                            if collidingItems.__len__() > 0:
                                player.addItemToInventory(collidingItems[0])

                                del globals.items[collidingItemsIndexes[0]]

                        for slotBinding in getSlotBindings():
                            if event.key == getattr(bindings, slotBinding[0]):
                                player.selectedInventorySlot = slotBinding[1] - 1

                                CurrentInventorySlotChangeEvent().child.call(player)
            else:
                globals.hasStartedDungeon = True
                roommanager.setRoom(roommanager.rooms[0])
        else:
            globals.hasStartedGame = True