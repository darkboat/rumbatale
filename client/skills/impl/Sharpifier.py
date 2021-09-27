from ui.SkillsBar import SkillsBar

class Sharpifier:
    def __init__(self):
        self.bar = SkillsBar("Sharpifier", 20, 10)

    def draw(self, screen, fontmanager, x, y, guimanager):
        self.bar.draw(screen, fontmanager, x, y, guimanager)