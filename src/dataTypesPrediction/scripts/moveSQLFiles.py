#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
rootdir = '/home/hager/college/GP/data types prediction/yale university/cosql_dataset/database'

def moveFiles(oldDirectory,newDirectory):
    index = 0
    for subdir, dirs, files in os.walk(oldDirectory):
        for file in files:
            if(file.split('.')[-1] == 'sql'):
                name = "/schema"
                os.rename(os.path.join(subdir, file), newDirectory+name+str(index)+".sql")
                index+=1


def main():
    if len(sys.argv)<2:
        print("Enter the directory of the schemas and the directory of the output file.")
    else:  
        moveFiles(str(sys.argv[1]),str(sys.argv[2]))

        
if __name__ == "__main__":
    main()