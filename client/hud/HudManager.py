from client.hud.impl.AbilityHud import AbilityHud

class HudManager:
    def __init__(self):
        self.hudmods = []

        self.addMod(AbilityHud())

    def addMod(self, mod):
        self.hudmods.append(mod)

    def draw(self, screen):
        print(self.hudmods)
        for mod in self.hudmods:
            if mod.enabled:
                mod.draw(screen)

hudmanager = HudManager()