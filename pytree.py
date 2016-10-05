#!/usr/bin/env python3
import subprocess
import sys
import os
import string

# YOUR CODE GOES here
def buildTree(curPath, prefix):
    files = []
    for fileName in os.listdir(curPath):
        if fileName[0] != '.':
            files.append(fileName)
    # sort all the files
    files.sort()
    # print (files)
    dirNum = 0
    FileNum = 0
    for index in range(len(files)):
        fileName = files[index]
        if index < len(files) - 1:
            curPrefix = "├── "
            subPrefix = "│   "
        else:
            curPrefix = "└── "
            subPrefix = "    "
        print(prefix + curPrefix + fileName)
        if os.path.isfile(os.path.join(curPath, fileName)):
            FileNum += 1
        else:
            dirNum += 1
            # recursively call buildTree
            tempdirNum, tempFileNum = buildTree(os.path.join(curPath, fileName), prefix + subPrefix)
            dirNum += tempdirNum
            FileNum += tempFileNum
    return dirNum, FileNum



def printTree(path):
    print(path)

    Numdir, Numfile = buildTree(path, "")

    print()
    if Numdir != 1:
        dirName = " directories, "
    else:
        dirName = " directory, "
    if Numfile != 1:
        fileName = " files"
    else:
        fileName = " file"

    print(str(Numdir) + dirName + str(Numfile) + fileName)



#main
if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])

    #error check
    if (len(sys.argv) > 2):
        print("Invalid.")
        sys.exit()

   
    if len(sys.argv) == 2:
        printTree(sys.argv[1]);
    else:
    	printTree('.');		#by default, open root directry