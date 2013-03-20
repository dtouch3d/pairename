#!/usr/bin/python

import os
import sys
import argparse
"""
parser = argparse.ArgumentParser(description='Renames files to match respective video file names (Default: srt)')

parser.add_argument('--extension', nargs=1, default='srt', dest=ext)
parser.add_argument('--matching', nargs=1, default='avi', dest=matching)
parser.add_argument('--debug', action='store_true', help='dry run, print debug messages')
"""

# TODO: argparser, verbose ?
#       Eliminate ext1,2 altogether ?
if len(sys.argv) != 4:
  print("subrename.py <target folder> <extension1> <extension2>")
  print("Renames files with ext1 with the name of the respective  alphabetical order of ext2")
  sys.exit(0)

path = sys.argv[1]
ext1 = sys.argv[2]
ext2 = sys.argv[3]

pwd = os.path.realpath(path)
os.chdir(pwd)

ls = os.listdir(pwd)

ext1List = [x for x in ls if ext1 in x]
ext1List.sort()

ext2List = [x for x in ls if ext2 in x]
ext2List.sort()

print("ext1List: " + str(ext1List))
print("ext2List: " + str(ext2List))

ext2ListNew = [os.path.splitext(x)[0] + "." + ext2 for x in ext1List]
print("ext2ListNew:", ext2ListNew)

for ext2, ext2New in zip(ext2List, ext2ListNew):
  print("Renaming " + ext2 + " to " + ext2New)
  os.rename(ext2, ext2New)
