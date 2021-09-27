class GUICompletedGame:
    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        endGameMessage = "YOU HAVE COMPLETED THE GAME!"
        screen.blit(fontmanager.titleText.render(endGameMessage, False, (0, 255, 0)), (screenwidth - (endGameMessage.__len__() * 25) - 50, screenheight / 2 - 100))
        screen.blit(fontmanager.hudText.render("Press any key to continue..", False, (0, 255, 0)), (screenwidth - (endGameMessage.__len__() * 25) + 125, screenheight / 2))