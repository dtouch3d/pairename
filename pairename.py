#!/usr/bin/python

import os
import sys
import argparse

cmd_args = None


def dbg(*args):
    if cmd_args.verbose or cmd_args.dry:
        sys.stdout.write('[DEBUG]: ')
        for arg in args:
            sys.stdout.write(str(arg))
        print()


def get_args():

    parser = argparse.ArgumentParser(
            description='Renames files of one extension to '
                        'match the file names of the other')
    parser.add_argument('-m', action="store", dest="matchingExt", help=
                        'extension of the filenames you want to rename to')
    parser.add_argument('-r', action="store", dest="toRenameExt", help=
                        'extension of the files you want to rename')
    parser.add_argument('-d', action="store", dest='path', help=
                        'target directory containing the files '
                        'you want to rename', default=os.getcwd())
    parser.add_argument('--dry', action="store_true", dest='dry', help=
                        'renames nothing, prints debug messages')
    parser.add_argument('--verbose', action="store_true", dest='verbose', help=
                        'verbose, prints debug messages')
    parser.add_argument('--revert', action="store_true", dest='revert', help=
                        'restores previously changed file names')
    parser.add_argument('--version', action="version", version='%(prog)s 0.6')

    return parser.parse_args()


def main():
    global cmd_args
    cmd_args = get_args()

    matchingExt = cmd_args.matchingExt
    toRenameExt = cmd_args.toRenameExt
    path = cmd_args.path

    if (matchingExt is None or toRenameExt is None) and not cmd_args.revert:
        print('Not enough arguments! (-h for help)')
        sys.exit(1)

    pwd = os.path.realpath(path)
    os.chdir(pwd)

    ls = os.listdir(pwd)

    matchingExtList = sorted([x for x in ls if matchingExt in x])
    toRenameExtList = sorted([x for x in ls if toRenameExt in x])
    toRenameExtListNew = [os.path.splitext(x)[0] + "." + toRenameExt
                          for x in matchingExtList]

    dbg("Files to rename: ", str(toRenameExtList))
    dbg("Matching: ", str(matchingExtList))
    dbg("New file names: ", toRenameExtListNew)

    for toRenameExt, toRenameExtNew in zip(toRenameExtList, toRenameExtListNew):
        dbg(toRenameExt, " --> ", toRenameExtNew)
        if not cmd_args.dry:
            os.rename(toRenameExt, toRenameExtNew)

if __name__ == '__main__':
    main()
