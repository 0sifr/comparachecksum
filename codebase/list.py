#!/usr/bin/env python

import sys
import os

for folder in sys.argv[1:]:
    fileList=[os.listdir(folder)]

folder=sys.argv[1:]

for s in fileList:
    fullpath = (folder + s)

for s in fileList:
    fullpath = map(lambda orig_string: folder + orig_string, fileList)

print(fullpath)
