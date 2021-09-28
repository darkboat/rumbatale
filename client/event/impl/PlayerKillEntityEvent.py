from client.event.Event import Event

class PlayerKillEntityEvent(Event):
    def __init__(self):
        super().__init__(self)

    def call(self, entity, player):
        reward = (int(entity.MaxHealth * entity.meleeDamage / 100))
        player.exp += reward

        entity.spawnRandomDrop(entity.posX, entity.posY)