from globals import globals

class Button:
    def __init__(self, fontmanager, x, y, w, h, text):
        self.surface = fontmanager.hudText.render(text, False, (0, 255, 0))

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.listener = None

        self.addedToGlobals = False
        
    def setOnClickListener(self, listener):
        if not self.addedToGlobals:
            self.listener = listener

            globals.buttons.append(self)

            self.addedToGlobals = True

    def onClick(self, mouse):
        if self.listener != None:
            x = mouse.pos[0]
            y = mouse.pos[1]

            if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
                self.listener(mouse)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))