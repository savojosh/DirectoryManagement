# get the directory
# list the directory's contents
# unzip/decompress all contents that are .zip, .tar.gz, .tgz, .tar, and .7z

# extract tar
# extract zip


# Imports

import os
import sys
import zipfile
import tarfile
import shutil

# Traverses a directory and unpacks all content that is compressed or archived.
def traverse_directory(directory):
    
    index = 0
    didUnpack = False
    contents = os.listdir(directory)

    # Use a while loop to be able to manipulate content without risks of using a for loop
    # Emulates a C-family formatted for loop with an incrementing variable since Python isn't compatible with incrementing for loops
    while(index < len(contents)):

        # Current content to manipulate
        content = contents[index]
        # Path to current content
        contentPath = directory + "/" + content

        # If the content is a directory, recursively traverse through it
        if(os.path.isdir(contentPath)):
            traverse_directory(contentPath)

        # If the content is a file
        elif(os.path.isfile(contentPath)):

            # Determines if content file is compressed or archived

            if(content.endswith(".zip") or content.endswith(".7z")): # If compressed
                didUnpack = extract_zip(contentPath, (directory + "/" + content.split(".")[0])) # extract_zip(target, destination)
                if(didUnpack): os.remove(contentPath) # removes compressed file if successfully uncompressed

            elif(content.endswith(".tar") or content.endswith(".tgz") or content.endswith(".tar.gz")): # If archived
                # TODO: change False to argv input
                didUnpack = extract_tar(contentPath, (directory + "/" + content.split(".")[0]), False) # extract_tar(target, destination, want resulting structure?)
                if(didUnpack): os.remove(contentPath) # removes archived file if successfully unarchived

        index = index + 1

    # If no failures in unpacking, traverse through directory again to check for content to unpack within previously unpacked content
    if(didUnpack):
        traverse_directory(directory)

# Extract zip content
def extract_zip(target, destination):
    try:
        # Extracts the zip contents
        with zipfile.ZipFile(target, "r") as zip:
            zip.extractall(destination)
            zip.close()
        return True

    except:
        print("Failed to extract zip file: " + target)

    return False

# Extract tar contents
def extract_tar(target, destination, structure):

    # tar -xvf 1.tar --strip-components=<num_directories> <target_directory>

    try:
        # Extracts the tar contents
        with tarfile.open(target, "r") as tar:
            tar.extractall(destination)
            if(not structure): 
                remove_tar_structure(destination)
            tar.close()
        return True

    except:
        print("Failed to extract tar file: " + target)

    return False

# Removes resulting directory structure from unpacking a tar archive
def remove_tar_structure(destination):
    destinationStructure = destination.split("/")
    currentPath = destination
    desiredPosition = destinationStructure[len(destinationStructure) - 1]
    directoryPosition = ""
    structureToDelete = ""

    # Determines what directory structure to delete based on operating system directory structure features
    
    if(destinationStructure[0].find(":") == -1): # if the operating system is not windows...
        structureToDelete = destinationStructure[0]
    else: # the operating system is windows...
        structureToDelete = destinationStructure[1]

    # Loops until finds the desired directory to extract content from
    while(desiredPosition != directoryPosition):
        directoryPosition = os.listdir(currentPath)[0]
        currentPath = currentPath + "/" + directoryPosition

    # Moves contents to desired destination
    for content in os.listdir(currentPath):
        shutil.move((currentPath + "/" + content), (destination + "/" + content))

    # Removes directory and all subdirectories and files within said directory
    shutil.rmtree(destination + "/" + structureToDelete)

# Traverses inputted directory
# TODO: add argv input
traverse_directory("C:/Users/savojess/Documents/Joshua/TestFiles")