#!/bin/bash -

<<COMMENT
for f in *.mkv; do
      CURRENT_VID = `echo $f | sed -e 's/.srt//' `
      ID = `echo $CURRENT_VID | grep -o [Ss][[:digit:]].[Ee][[:digit:]].`
      SUB = `ls *.srt | grep $ID`
      echo $CURRENT_VID
      echo $ID
      echo $SUB
      cp $SUB $CURRENT_VID.srt
done
COMMENT
