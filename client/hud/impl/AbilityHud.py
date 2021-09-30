from client.hud.HudMod import HudMod

import pygame


class AbilityHud(HudMod):
    def __init__(self):
        super().__init__("AbilityHud", 0, 0, 200, 100)

    def draw(self, screen):
        print(1)
        print(super().x, super().y)
        pygame.draw.rect(screen, (255, 255, 255), (super().x, super().y, super().w, super().h)) 