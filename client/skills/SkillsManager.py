from skills.impl.Protection import Protection
from skills.impl.Sharpifier import Sharpifier

class SkillsManager:
    def __init__(self):
        self.skills = []

        self.skills.append(Sharpifier())
        self.skills.append(Protection())

    def draw(self, screen, fontmanager, guimanager):
        yIndex = 0
        for skill in self.skills:
            skill.draw(screen, fontmanager, 50, 200 + (75 * yIndex), guimanager)

            yIndex += 1

    def getSkill(self, skill_name):
        res = []
        [res.append(x) for x in self.skills if x.bar.name == skill_name]

        return res[0]

skillsmanager = SkillsManager()