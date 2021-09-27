from skills.SkillsManager import skillsmanager

from globals import globals

class GUISkillsMenu:
    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        screen.blit(fontmanager.titleText.render("Skills Menu", False, (0, 255, 0)), (25, 25))
        screen.blit(fontmanager.titleText.render(str(globals.player[0].exp) + "EXP", False, (0, 255, 0)), (25, 100))

        skillsmanager.draw(screen, fontmanager, guimanager)