#!/usr/bin/python
import random, os, sys
  
def randomize_file(path):
    random.seed()
    with open(path, "r+b") as file:
        len = os.path.getsize(path)
        for byte in xrange(len):
            file.write(str(random.randrange(9)))
            

def main (path):
    if os.path.isdir(path):
        print("Path is a directory.  Function not implemented.")
    elif os.path.isfile(path):
        print("Randomizing file: " + os.path.abspath(path))
        randomize_file(path)
    else:
        print("Invalid path: " + path)

if __name__ == "__main__" :
    if sys.argv.__len__() == 2 :
        path = sys.argv[1]
        main(path)
    else :
        print("Incorrect arguments")