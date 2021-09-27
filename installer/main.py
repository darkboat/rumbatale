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

shutil.rmtree(outDir, ignore_errors=True)

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


for i in os.listdir(outDir):
    if i.endswith('git'):
        tmp = os.path.join(outDir, i)
        # We want to unhide the .git folder before unlinking it.
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)


while True:
    if len(os.listdir(outDir)) == 0:
        Repo.clone_from("https://github.com/darkboat/rumbatale.git", outDir)
        
        shutil.rmtree(outDir + "/installer") # remove unwanted folder from repository

        # ENDING OF INSTALLATIOn
        break
    else:
        time.sleep(0.001)