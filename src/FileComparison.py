"""
Python Edition
"""

#----- IMPORTS -----#

from multiprocessing.reduction import duplicate
import os
from pathlib import Path
from filecmp import cmp

def findDuplicates(dir):

    files = os.listdir(dir)

    for file in files:
        if(os.path.isdir(file)):
            findDuplicates(file)
        else:
            pass

#findDuplicates("C:\Users\savojess\Documents\Joshua\TestFiles")

DATA_DIR = Path('C:/Users/savojess/Documents/Joshua/TestFiles')
files = sorted(os.listdir(DATA_DIR))

duplicateFiles = []

for file in files:

    if_dupl = False

    for class_ in duplicateFiles:

        if_dupl = cmp(
            DATA_DIR / file,
            DATA_DIR / class_[0],
            shallow = True
        )

        if if_dupl:
            class_.append(file)
            break
    
    if not if_dupl:
        duplicateFiles.append([file])

print(duplicateFiles)