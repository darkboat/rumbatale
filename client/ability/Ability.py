class Ability:
    def __init__(self, name, manaCost, runFunction):
        self.name = name
        self.cost = manaCost
        self.childRun = runFunction

    def run(self, player):
        self.childRun(player)

    def defaultFinish(self, player):
        if player.mana - self.cost >= 0:
            player.mana -= self.cost