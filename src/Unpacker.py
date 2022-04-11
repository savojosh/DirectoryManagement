# get the directory
# list the directory's contents
# unzip/decompress all contents that are .zip, .tar.gz, .tgz, .tar, and .7z

# extract tar
# extract zip


# Imports

from operator import contains
import os
import sys
import zipfile
import tarfile
import shutil

def traverse_directory(directory):
    
    index = 0
    didUnzip = False
    contents = os.listdir(directory)

    while(index < len(contents)):

        content = contents[index]
        contentPath = directory + "/" + content

        print(content)
        
        if(os.path.isdir(contentPath)):
            traverse_directory(contentPath)

        elif(os.path.isfile(contentPath)):

            if(content.endswith(".zip") or content.endswith(".7z")):
                didUnzip = extract_zip(contentPath, (directory + "/" + content.split(".")[0]))
                if(didUnzip): os.remove(contentPath)
            elif(content.endswith(".tar") or content.endswith(".tgz") or content.endswith(".tar.gz")):
                didUnzip = extract_tar(contentPath, (directory + "/" + content.split(".")[0]), False)
                if(didUnzip): os.remove(contentPath)

        index = index + 1

    if(didUnzip):
        traverse_directory(directory)

def extract_zip(target, destination):
    try:
        with zipfile.ZipFile(target, "r") as zip:
            zip.extractall(destination)
            zip.close()
        return True

    except:
        print("Failed to extract zip file: " + target)

    return False

def extract_tar(target, destination, structure):

    # tar -xvf 1.tar --strip-components=<num_directories> <target_directory>

    try:
        with tarfile.open(target, "r") as tar:
            tar.extractall(destination)
            if(not structure): 
                remove_tar_structure(destination)
            tar.close()
        return True

    except:
        print("Failed to extract tar file: " + target)

    return False

def remove_tar_structure(destination):
    destinationStructure = destination.split("/")
    currentPath = destination
    desiredPosition = destinationStructure[len(destinationStructure) - 1]
    directoryPosition = ""
    structureToDelete = ""

    if(destinationStructure[0].find(":") == -1): # if the operating system is not windows...
        structureToDelete = destinationStructure[0]
    else: # the operating system is windows...
        structureToDelete = destinationStructure[1]

    while(desiredPosition != directoryPosition):

        directoryPosition = os.listdir(currentPath)[0]
        currentPath = currentPath + "/" + directoryPosition

    for content in os.listdir(currentPath):

        shutil.move((currentPath + "/" + content), (destination + "/" + content))

    shutil.rmtree(destination + "/" + structureToDelete)

traverse_directory("C:/Users/savojess/Documents/Joshua/TestFiles")
                   #C:/Users/savojess/Documents/Joshua/TestFiles/tarmynuts/Users/savojess/Documents/Joshua/TestFiles/tarmynuts