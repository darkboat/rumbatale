from client.ui.SkillsBar import SkillsBar

class Protection:
    def __init__(self):
        self.bar = SkillsBar("Protection", 10, 10)

    def draw(self, screen, fontmanager, x, y, guimanager):
        self.bar.draw(screen, fontmanager, x, y, guimanager)