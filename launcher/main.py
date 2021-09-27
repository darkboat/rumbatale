import os

def launch():
    appdata = os.getenv("APPDATA")
    gameDir = str(appdata) + "/.rumbatale/client"

    os.system(gameDir + "/dist/main.exe")

launch()