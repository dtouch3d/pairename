#!/bin/bash -

if [ $# -ne 2 ]; then 
  echo gsub v0.0.2 : GreekSubtitles.info downloader
  echo Usage: gsub \<"search string in quotes"\> \<destination folder\>
  exit 1
fi

# Example URL : http://www.greeksubtitles.info/search.php?name=whaat+up+doc

search_str=`echo $1 | sed -e "s/\"//" | sed -e "s/\ /+/g"`

cd $2

wget http://www.greeksubtitles.info/search.php?name=$search_str -O search.html

echo [+] Downloading 
for i in `grep -o get_greek.* search.html | cut -d "'" -f1 | cut -d "?" -f2`; do
  wget http://www.findsubtitles.eu/getp.php?$i -P $2 -O $i 
done

echo [+] Extracting 
for i in $2/getp*; do
  unrar x -o+ $i > /dev/null
done

echo [+] Cleaning up
for i in $2/getp*; do
  rm $i
done

rm search.html xsubs.tv.url
