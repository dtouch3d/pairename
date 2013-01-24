#!/bin/bash
EP_REGEX='.*[sS]*[0-9]+[xeE][0-9]+.*'
VID="$EP_REGEX"'.(avi|mkv)'
SUB="$EP_REGEX"'.(srt|idx|sub)'

for i in $(find . -maxdepth 1 -regextype posix-egrep -iregex "$VID"); do
  # find corresponding srt
  ep=$(echo $i | grep -E -i -o "$EP_REGEX")
  sub=$(find . -maxdepth 1 -regextype posix-egrep -iregex "$SUB")

  if [ $1 == "debug" ]
    then
      echo video file: $i
      echo ep code is: $ep
      echo new name of sub: $sub
      exit
  fi

  if [ -n sub ]
    then
    
    IFS=$','
    # rename it!
    mv $sub $(basename "$i" .avi).srt
    unset IFS
  
  fi

done
