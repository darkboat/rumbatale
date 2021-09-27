class GUIEnterDungeon:
    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        message = "Press any key to enter the dungeon.."
        screen.blit(fontmanager.titleText.render(message, False, (0, 255, 0)), (screenwidth - (message.__len__() * 25) + 110, screenheight / 2 - 100))