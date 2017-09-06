#!/bin/bash

operation=$1

if [ $# -lt 2 ]; then
  echo "Too few parameters. Usage: [operation] [integer1] [integer2] ..."
  exit
fi

if [ $operation == "S" ]; then
  echo "Sum"
elif [ $operation == "P" ]; then
  echo "Product"
elif [ $operation == "M" ]; then
  echo "Maximum"
elif [ $operation == "m" ]; then
  echo "Minimun"
else
  echo "Wrong operation code: $operation. Use S, P, M, m"
fi


# declare -i n; n=1
# for arg in $@; do
#   echo "command-line argument no. $n is <$arg>"
#   ((n++))
# done
