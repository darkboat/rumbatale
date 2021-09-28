import pygame

from client.globals import globals

class TextInput:
    def __init__(self, x, y, w, h, prev):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.prev = prev

        self.enabled = False
        self.activated = False

        self.text = ""

        self.listener = lambda text: print()

        self.preventDef = False

        globals.textinputs.append(self)

    def preventDefault(self):
        self.preventDef = True

    def draw(self, screen, fontmanager):
        pygame.draw.rect(screen, (79, 79, 79), (self.x, self.y, self.w, self.h))
        screen.blit(fontmanager.textInput.render(self.text if len(self.text) > 0 else self.prev, False, (255, 255, 255)), (self.x + 15, self.y + 17.5))

    def setOnReturnListener(self, listener):
        self.listener = listener

    def onType(self, event):
        if self.activated and self.enabled:
            if event.key == pygame.K_RETURN:
                self.listener(self.text)

                if not self.preventDef:
                    self.text = ""

            elif event.key == pygame.K_BACKSPACE:
                if len(self.text) > 0:
                    self.text = self.text[:len(self.text) - 1]

            else:
                self.text += event.unicode

    def onPress(self, event):
        posX = event.pos[0]
        posY = event.pos[1]

        mouseRect = pygame.Rect(posX, posY, 1, 1)

        selfRect = pygame.Rect(self.x, self.y, self.w, self.h)

        if mouseRect.colliderect(selfRect):
            for textinput in globals.textinputs:
                textinput.activated = False

            self.activated = True