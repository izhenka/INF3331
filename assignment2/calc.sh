#!/bin/bash

operation=$1;
shift;

if [ $# -lt 2 ]; then
  echo "Too few parameters. Usage: [operation] [integer1] [integer2] ..."
  exit
fi


declare -i res; res=$1; shift;

for arg in $@; do
  case "$operation" in
    S)
      ((res+=arg)) ;;
    P)
      ((res*=arg)) ;;
    M)
      echo "Hui" ;;
    *)
     echo "$0: invalid option \"$operation\""; exit ;;
   esac
done


echo $res
