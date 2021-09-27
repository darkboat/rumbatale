class Craftable:
    def __init__(self, item, recipe, craftingmanager):
        craftingmanager.addCraftingItem([recipe, item])