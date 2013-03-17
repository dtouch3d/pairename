#!/usr/bin/python

import os
import sys

if len(sys.argv) != 4:
  print("subrename.py <target folder> <extension1> <extension2>")
  sys.exit(0)

pwd = sys.argv[1]
ext1 = sys.argv[2]
ext2 = sys.argv[3]

os.chdir(pwd)

ls = os.listdir(pwd)

ext1List = [x for x in ls if ext1 in x].sort()
ext2List = [x for x in ls if ext2 in x].sort()

print("ext1List: " + str(ext1List))
print("ext2List: " + str(ext2List))

ext2ListNew = [x.replace(ext1, ext2) for x in ext1List]

for ext2, ext2New in zip(ext2List, ext2ListNew):
  print("Renaming " + ext2 + " to " + ext2New)
  os.rename(ext2, ext2New)
