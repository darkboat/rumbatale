import pygame

class GUIDead:
    @staticmethod
    def draw(screen, fontmanager, screenwidth, screenheight, player, guimanager):
        message = "YOU DIED!"
        screen.blit(fontmanager.titleText.render(message, False, (0, 255, 0)), (screenwidth - (message.__len__() * 25) - 275, screenheight / 2 - 100))
        screen.blit(fontmanager.hudText.render("Press any key to continue...", False, (0, 255, 0)), (screenwidth - (message.__len__() * 25) - 325, screenheight / 2))

        pygame.quit()