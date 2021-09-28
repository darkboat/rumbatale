from os import stat
from client.ui.TextInput import TextInput
from client.crafting.CraftingManager import craftingmanager

class GUICraftingMenu:
    textInput = TextInput(100, 100, 200, 50, "Item To Craft")

    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        screen.blit(fontmanager.titleText.render("Crafting Menu", False, (0, 255, 0)), (25, 25))

        GUICraftingMenu.textInput.setOnReturnListener(lambda text: GUICraftingMenu.onEnter(player, text))
        GUICraftingMenu.textInput.draw(screen,fontmanager)

    @staticmethod
    def onEnter(player, itemName):
        items = craftingmanager.getCraftableItems(player)

        found = None
        
        for item in items:
            name = item[1].__name__

            if itemName == name:
                found = item

        if found != None:
            hasRequirements = False

            for req in found[0]:
                if player.hasItemInInventory(req):
                    hasRequirements = True

                else:
                    hasRequirements = False

            if hasRequirements:
                for req in found[0]:
                    toDelete = []
                    i = 0
                    for slot in player.inventory:
                        if slot != None:
                            if isinstance(slot, req):
                                toDelete.append(i)

                        i += 1

                    for delete in toDelete:
                        player.inventory[delete] = None

                item = found[1](0, 0)

                player.addItemToNextFreeSlot(item)