from client.skills.SkillsManager import skillsmanager
from client.entities.impl.Enemy import Enemy
from client.entities.StatBuilder import StatBuilder
from client.drops.presets.enemies.Crawler import drops as CrawlerDrops
import client.client_globals as cGlobals

class Crawler(Enemy):
    def __init__(self, pos):
        self.tick = 0
        super().__init__(StatBuilder(MeleeDamage=15, SpellDamage=0, Health=100), "Crawler", pos, 0.02)

        super().initDropTable(CrawlerDrops)

    def Tick(self, player):
        self.tick += 1

        if not self.shocked:
            if self.posX > (player.posX + cGlobals.cameraX):
                self.posX -= self.speed
            elif self.posX < (player.posX + cGlobals.cameraX):
                self.posX += self.speed

            
            if self.posY > (player.posY + cGlobals.cameraY):
                self.posY -= self.speed
            elif self.posY < (player.posY + cGlobals.cameraY):
                self.posY += self.speed

            if self.tick >= 1000:
                if not player.invincible:       
                    selfRect = self.getScreenRect()
                    pRect = player.getRect()

                    if selfRect.colliderect(pRect):
                        totalDamage = (self.meleeDamage / float("1." + str(skillsmanager.getSkill("Protection").bar.level)))

                        player.health -= round(totalDamage/0.5) * 0.5

                        if player.health <= 0:
                            player.isDead = True


                self.tick = 0