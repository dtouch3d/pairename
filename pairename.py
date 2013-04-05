#!/usr/bin/python

import os
import sys
import argparse


parser = argparse.ArgumentParser(description=
         'Renames files of one extension to match name of the other'
         'Target folder must hold only two kinds of files.')

parser.add_argument('-m', action="store", dest="matchingExt", help=
                    'The extension of the filenames you want to rename to')
parser.add_argument('-r', action="store", dest="toRenameExt", help=
                    'The extension of the files you want to rename')

print(parser.parse_args())

# parser.add_argument('--debug', action='store_true', help='dry run, print debug messages')


# TODO: argparser, verbose ?
#       Eliminate matchingExt,2 altogether ?
#       Backup / revert changes ?
#       Auto find extensions

if len(sys.argv) != 4:
    print("subrename.py <target folder> <toRenameExt> <matchingExt>\n"
          "Renames files with matchingExt with the name of the respective "
          "alphabetical order of toRenameExt")
    sys.exit(0)

path = sys.argv[1]
matchingExt = sys.argv[2]   # matching extension
toRenameExt = sys.argv[3]   # rename files with this extension

pwd = os.path.realpath(path)
os.chdir(pwd)

ls = os.listdir(pwd)

matchingExtList = [x for x in ls if matchingExt in x]
matchingExtList.sort()

toRenameExtList = [x for x in ls if toRenameExt in x]
toRenameExtList.sort()

print("matchingExtList: ", str(matchingExtList))
print("toRenameExtList: ", str(toRenameExtList))

toRenameExtListNew = [os.path.splitext(x)[0] + "." + toRenameExt
                     for x in matchingExtList]

print("toRenameExtListNew:", toRenameExtListNew)

for toRenameExt, toRenameExtNew in zip(toRenameExtList, toRenameExtListNew):
    print("Renaming " + toRenameExt + " to " + toRenameExtNew)
    os.rename(toRenameExt, toRenameExtNew)
