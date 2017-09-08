#!/bin/bash
function exp {
  echo "$1->$2"
  export $1=$2
}

echo "Initializing variables..."

while read p; do
  var_value=`echo $p | awk 'BEGIN { FS="|"; } {print $1, $2}'`
  exp $var_value
done < $HOME/.bookmarks

echo "...Done"
