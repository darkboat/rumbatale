class globals:
    isRunning = True
    hasStartedGame = False
    hasStartedDungeon = False
    hasCompletedDungeon = False

    hasSkillsMenuOpen = False
    hasCraftingMenuOpen = False
    hasEnchantingMenuOpen = False

    ability1 = None
    ability2 = None
    ability3 = None
    ability4 = None

    entities = []
    enemies = []
    items = []
    player = []

    buttons = []
    textinputs = []

    buffs = []
    timedChanges = []

    currentGUI = None

def toJSON():
    return globals.__dict__