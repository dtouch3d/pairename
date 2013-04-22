pairename
==========

Renames pairs of files with different extension to the same name. Useful for subtitles and maybe more.

Currently it matches pairs of files based on the alphabetical order of the two kinds of files. Fuzzy string matching is on the way.

```
usage: pairename.py [-h] [-m MATCHINGEXT] [-r TORENAMEEXT] [-d PATH] [--dry]
                    [-verbose] [--version]
optional arguments:
  -h, --help      show this help message and exit
  -m MATCHINGEXT  extension of the filenames you want to rename to
  -r TORENAMEEXT  extension of the files you want to rename
  -d PATH         target directory containing the files you want to rename
  --dry           renames nothing, prints debug messages
  --verbose        verbose, prints debug messages
  --version       show program's version number and exiHPE 87
```
