#!/bin/bash
function exp {
  echo "$1->$2"
  export $1=$2
}


if [ $# -eq 1 ]; then
  echo "$0: Wrong use of parameters. Usage: [operation bookmarkname]"
  return 1;
fi


if [ "$1" == "-r" ]; then
  # removing
  bookmarkname=$2
  unset $bookmarkname
  echo "Unsetting $bookmarkname"

  while read p; do
    var_name=`echo $p | awk 'BEGIN { FS="|"; } {print $1}'`
    if [ "$var_name" != "$bookmarkname" ]; then
      echo $p
    fi
  done < $HOME/.bookmarks > tmp

  cat tmp > $HOME/.bookmarks
  rm tmp
elif [ "$1" == "-a" ]; then
  # adding new bookmark
  cur_path=`pwd`
  echo "$2|$cur_path" >> $HOME/.bookmarks
elif [ "$1" != "" ]; then
  echo "$0: invalid option \"$1\""
  return 1
fi


# Initializing
echo "Initializing variables..."
while read p; do
  var_value=`echo $p | awk 'BEGIN { FS="|"; } {print $1, $2}'`
  exp $var_value
done < $HOME/.bookmarks
echo "...Done"
