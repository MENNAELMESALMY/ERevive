import os
import sys


    
def unzipRepos():
    repos_files = os.listdir('./repos')
    for repos_file in repos_files:
        #unzip repos_file in repos folder
        os.system('unzip -o ./repos/' + repos_file + ' -d ./repos_unzipped/')
        #get the name of the file


def traversRepoFiles(root):
    for path, dirs, files in os.walk(root):
        for file in files:
            if file.endswith('.sql'):
                os.system('cp ' + path + '/' + file + ' ./sql_files/')
    

def getSqlRepos(repospath):
    repos = os.listdir(repospath)
    for repo in repos:
        traversRepoFiles( repospath+ repo)
    
#unzipRepos()
getSqlRepos('./repos_unzipped/')   