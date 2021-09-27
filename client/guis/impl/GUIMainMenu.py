class GUIMainMenu:
    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        message = "Welcome to RUMBATALE!"
        screen.blit(fontmanager.titleText.render("Welcome to RUMBATALE!", False, (0, 255, 0)), (screenwidth - (message.__len__() * 25) - 135, screenheight / 2 - 100))
        screen.blit(fontmanager.hudText.render("Press any key to continue..", False, (0, 255, 0)), (screenwidth - (message.__len__() * 25) - 25, screenheight / 2))
