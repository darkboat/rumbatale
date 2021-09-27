from guis.impl.GUIEnchantingMenu import GUIEnchantingMenu
from guis.impl.GUICraftingMenu import GUICraftingMenu


class GuiManager:
    def __init__(self):
        self.currentGUI = None

    def setGUI(self, GUI):
        self.currentGUI = GUI

        if GUI is GUICraftingMenu:
            GUICraftingMenu.textInput.enabled = True

        else:
            GUICraftingMenu.textInput.enabled = False

        if GUI is GUIEnchantingMenu:
            GUIEnchantingMenu.enchantment.enabled = True
            GUIEnchantingMenu.item.enabled = True

        else:
            GUIEnchantingMenu.enchantment.enabled = False
            GUIEnchantingMenu.item.enabled = False

    def drawGUI(self, screen, fontmanager, screenwidth, screenheight, player, guimanager):
        if self.currentGUI != None:
            self.currentGUI.draw(screen, fontmanager, screenwidth, screenheight, player, guimanager)