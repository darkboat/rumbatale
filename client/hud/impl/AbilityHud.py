from client.hud.HudMod import HudMod

import pygame


class AbilityHud(HudMod):
    def __init__(self):
        super().__init__("AbilityHud", 200, 600, 200, 100)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.w, self.h))