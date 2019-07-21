#!/usr/bin/env python3

'''
This python code asks for two directories, calculates the checksums of all
files found inside the two directories and then lists the two sets of checksums
so that they can be compared
'''

import os
import hashlib
import sys
from pprint import pprint

currentDir = os.path.abspath(os.curdir) #state current working directory
file_list_dict = {} #create dictionary


folder =  [sys.argv[1:], sys.argv[2:]]
folder = ["/home/user/pwds/", "/home/user/Pictures/"]

import easygui
for i in range(2):
###    folder = currentDir
    os.chdir(folder[i])			#move current working directory to folder
##    folder = sys.argv[i+1:]
#    for folder in sys.argv[i:]:
#        folder = [os.listdir(folder)]
###    message = "Select folder " + str(i)
###    folder = easygui.diropenbox(msg=message, title=None, default=folder)
    file_list_dict[folder[i]] = list(filter(os.path.isfile, os.listdir(os.curdir))) #list only the files, not the folders


def sha256(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


for folder in file_list_dict:
    checksums = [] 
    files = file_list_dict[folder]
    os.chdir(folder)
    for filename in files:
        checksum = sha256(filename) #apply sha256 function to file
        checksums.append((filename, checksum))
    file_list_dict[folder] = checksums

pprint(file_list_dict)
#      print checksum + '\t' + filename
#    print "\n"

'''
To do:
- list identical files of the two folders one after the other (along with their checksums)
'''

loop through dict_key0
    if corresponding value = any value in dict_key1
        print the value
    print any remianing values



