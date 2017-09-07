#!/bin/bash

tz_code=$1

case "$tz_code" in
  no)
    timezone="Europe/Oslo" ;;
  sk)
    timezone="Asia/Seoul" ;;
  us)
    timezone="US/Eastern" ;;
  "")
    timezone="" ;;
  *)
    echo "$0: invalid option \"$operation\""; exit ;;
  esac



while [ "1" ]
do
  clear
  TZ="$timezone" date
  sleep 1
done
