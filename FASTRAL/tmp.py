import subprocess
import os
import warnings


warnings.warn("This is the first time you are using FASTRAL! Let's build dependencies...")
path = "ASTRAL-modified"
cm = "cd ../ASTRAL-modified \n sh make.sh"

p = subprocess.Popen(cm, shell=True)
(output, err) = p.communicate()
p_status = p.wait()
