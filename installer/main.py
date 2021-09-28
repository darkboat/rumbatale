from git import Repo

import os
import shutil
import time
import stat
from subprocess import call

def onerror(func, path, exc_info):
    import stat
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

appdata = os.getenv("APPDATA")
outDir = str(appdata) + "/.rumbatale"

print("deleting past install...")

shutil.rmtree(outDir, ignore_errors=True)

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

if os.path.exists(outDir):
    for i in os.listdir(outDir):
        if i.endswith('git'):
            tmp = os.path.join(outDir, i)
            while True:
                call(['attrib', '-H', tmp])
                break
            shutil.rmtree(tmp, onerror=on_rm_error)


while True:
    if (len(os.listdir(outDir)) == 0) if os.path.exists(outDir) else True:

        Repo.clone_from("https://github.com/darkboat/rumbatale.git", outDir)

        print("cloning repository...")
        
        shutil.rmtree(outDir + "/installer") # remove unwanted folder from repository
        
        print("cleaning up...")

        # ENDING OF INSTALLATION
        break
    else:
        time.sleep(0.001)