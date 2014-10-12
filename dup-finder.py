#!/usr/bin/python
import sys
import os
import hashlib

file_dict = {}
duplicate_dict = dict()

def hashfile(file, blocksize=65536):
    hasher = hashlib.sha256()
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    return hasher.hexdigest()

def findDups(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            fileabs = os.path.abspath(root) + "/" + name
            sha2 = hashfile(open(fileabs, 'rb'), 16384)
            if sha2 not in file_dict.keys() :
                file_dict[sha2] = fileabs
            else :
                addToDupDict(fileabs,sha2)


def addToDupDict(fileabs, sha2):
    if sha2 in duplicate_dict.keys() :
        duplicate_dict[sha2].append(fileabs)
    else :
        duplicate_dict[sha2] = [fileabs, file_dict[sha2]]

def printDupReport():
    print("Printing Dup Report...")
    if not any(duplicate_dict) :
        print("No duplicate files found.")
    else :
        for shas in duplicate_dict:
            print("Dup with Sha-2: " + shas) 
            for f in duplicate_dict[shas] :
                print(f)
    
def main(path) :
        findDups(path)
        printDupReport()
        print("Done examining path " + path)


if __name__ == "__main__" :
    if sys.argv.__len__() == 2 :
        path = sys.argv[1]
        if os.path.exists(path):
            print("Looking for duplicates on path: " + path)
            main(path)
        else:
            print("Invalid path: " + path)
        
                    
            
        
