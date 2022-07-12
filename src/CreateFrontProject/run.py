from cProfile import run
import os
from pathlib import Path

def run_front():

    print("start creating front project")
    os.system('chmod +rwx '+str(os.getcwd()))
    os.system('./CreateFrontProject.sh')
    front_path =  Path(os.getcwd()+'/FrontCode')
    os.chdir(str(front_path))
    os.system('npm run serve')

run_front()