import os
from pathlib import Path


def run_api():
    print("start creating api")
    directory_file = os.getcwd()
    api_path =  Path(directory_file) / Path('api')
    os.chdir(str(api_path))
    setup_file_path = Path(api_path) / Path('setup.sh')
    run_file_path = Path(api_path) / Path('run.sh')
    os.system('chmod +rwx ' + str(setup_file_path))
    os.system('chmod +rwx ' + str(run_file_path))
    os.system(str(setup_file_path))
    os.system(str(run_file_path))
run_api()