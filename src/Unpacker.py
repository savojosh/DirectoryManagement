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
                didUnzip = extract_tar(contentPath, (directory + "/" + content.split(".")[0]))
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

def extract_tar(target, destination):
    try:
        with tarfile.TarFile(target, "r") as tar:
            tar.extractall(destination)
            tar.close()
        return True

    except:
        print("Failed to extract tar file: " + target)

    return False

traverse_directory("C:/Users/savojess/Documents/Joshua/TestFiles")