from event.impl.CurrentInventorySlotChangeEvent import CurrentInventorySlotChangeEvent
import pygame
from event.Event import Event

import bindings
from globals import globals
import conf

class MouseDownEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, event, player):
        if event.button == 1:
            player.attack()

            for textinput in globals.textinputs:
                textinput.onPress(event)

        if event.button == 5:
            player.selectedInventorySlot += 1

            if player.selectedInventorySlot > conf.inventoryLength - 1:
                player.selectedInventorySlot = 0

            CurrentInventorySlotChangeEvent().child.call(player)

        if event.button == 4:
            player.selectedInventorySlot -= 1

            if player.selectedInventorySlot < 0:
                player.selectedInventorySlot = conf.inventoryLength - 1

        for button in globals.buttons:
            button.onClick(event)