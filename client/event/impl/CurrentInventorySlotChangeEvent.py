from client.event.Event import Event

class CurrentInventorySlotChangeEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, player):
        heldItem = player.getHeldItem()

        if hasattr(heldItem, "stats"):
            if hasattr(heldItem.stats, "abilities"):
                abilities = getattr(heldItem.stats, "abilities")

                player.ability1 = abilities[0]
                player.ability2 =  abilities[1]
                player.ability3 = abilities[2]
                player.ability4 = abilities[3]

        if heldItem == None:
            player.ability1 = None
            player.ability2 = None
            player.ability3 = None
            player.ability4 = None