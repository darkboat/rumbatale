class CraftingManager:
    def __init__(self) -> None:
        self.craftingItems = []

    def addCraftingItem(self, item):
        self.craftingItems.append(item)

    def getCraftingItems(self):
        return self.craftingItems

    def getCraftableItems(self, player):
        craftable = []

        for item in self.craftingItems:
            req = item[0]

            hasAllRequirements = False

            for i in req:
                if player.hasItemInInventory(i):
                    hasAllRequirements = True
                else:
                    hasAllRequirements = False

            if hasAllRequirements:
                craftable.append(item)

        return craftable

craftingmanager = CraftingManager()