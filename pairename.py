#!/usr/bin/python

import os
import sys
import argparse

# TODO: 
#       Backup / revert changes ?
#       Auto find extensions


parser = argparse.ArgumentParser(
        description='Renames files of one extension to match the file names of the other')

parser.add_argument('-m', action="store", dest="matchingExt", help=
                    'extension of the filenames you want to rename to')
parser.add_argument('-r', action="store", dest="toRenameExt", help=
                    'extension of the files you want to rename')
parser.add_argument('-d', action="store", dest='path', help=
                    'target directory containing the files you want to rename')
parser.add_argument('--dry', action="store_true", dest='dry', help=
                    'renames nothing, prints debug messages')
parser.add_argument('--verbose', action="store_true", dest='verbose', help=
                    'prints debug messages')
parser.add_argument('--version', action="version", version='%(prog)s 0.6')

cmd_args = parser.parse_args()

def dbg(*args):
    if cmd_args.dry or cmd_args.verbose:
        for arg in args:
            sys.stdout.write(str(arg))
        print()

# TODO: 
#       Backup / revert changes ?
#       Auto find extensions

matchingExt = cmd_args.matchingExt
toRenameExt = cmd_args.toRenameExt
path = cmd_args.path

if matchingExt is None or toRenameExt is None:
    print('Not enough arguments!')
    sys.exit(1)

pwd = os.path.realpath(path)
os.chdir(pwd)

ls = os.listdir(pwd)

cmd_args = parser.parse_args()

matchingExt = cmd_args.matchingExt
toRenameExt = cmd_args.toRenameExt
path = cmd_args.path

pwd = os.path.realpath(path)
os.chdir(pwd)

ls = os.listdir(pwd)

matchingExtList = [x for x in ls if matchingExt in x]
matchingExtList.sort()

toRenameExtList = [x for x in ls if toRenameExt in x]
toRenameExtList.sort()

toRenameExtListNew = [os.path.splitext(x)[0] + "." + toRenameExt
                     for x in matchingExtList]

dbg(path)
dbg("matchingExtList: ", str(matchingExtList))
dbg("toRenameExtList: ", str(toRenameExtList))
dbg("toRenameExtListNew:", toRenameExtListNew)

for toRenameExt, toRenameExtNew in zip(toRenameExtList, toRenameExtListNew):
    dbg("Renaming " + toRenameExt + " to " + toRenameExtNew)
    if not cmd_args.dry:
        os.rename(toRenameExt, toRenameExtNew)
