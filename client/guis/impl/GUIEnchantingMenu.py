from pygame import font
from client.ui.TextInput import TextInput
from client.ui.Button import Button

from client.items.enchantments.Enchantment import EnchantingBook

from client.globals import globals

class GUIEnchantingMenu:
    enchantment = TextInput(100, 200, 300, 50, "Enchantment")
    item = TextInput(100, 300, 300, 50, "item to enchant")

    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        GUIEnchantingMenu.enchantment.draw(screen, fontmanager)
        GUIEnchantingMenu.item.draw(screen, fontmanager)

        GUIEnchantingMenu.enchantment.preventDefault()
        GUIEnchantingMenu.item.preventDefault()

        enchantButton = Button(fontmanager, 100, 500, 300, 50, "Enchant")
        enchantButton.setOnClickListener(lambda mouse: GUIEnchantingMenu.onEnchant(player))
        enchantButton.draw(screen)

    @staticmethod
    def onEnchant(player):
        enchantment = None
        enchantmentIndex = None

        for i in range(len(player.inventory)):
            if isinstance(player.inventory[i], EnchantingBook):

                if type(player.inventory[i]).__name__.lower() == GUIEnchantingMenu.enchantment.text.strip().lower():
                    enchantment = player.inventory[i]
                    enchantmentIndex = i

                    break
        
        if enchantment != None:
            item = None

            for i in range(len(player.inventory)):
                correctType = False

                for t in enchantment.types:
                    if isinstance(player.inventory[i], t):
                        correctType = True

                if type(player.inventory[i]).__name__.lower() == GUIEnchantingMenu.item.text.strip().lower():
                    item = player.inventory[i]

                    break

            if item != None:
                enchantment.enchantItem(enchantment, item)
                globals.hasEnchantingMenuOpen = False

                player.inventory[enchantmentIndex] = None