#!/bin/bash
# A 'cookie' file is necessary

if [ -z "$1" ]; then
    day1=`date "+%e" | xargs`
else
    day1=$1
fi

day2=`printf %02d $day1`

if [ -z "$2" ]; then
    year=`date "+%Y"`
else
    year=$2
fi

cookie=`cat cookie`

curl "https://adventofcode.com/${year}/day/${day1}/input" \
    -o inputs/day${day2}.txt \
    --header "${cookie}"

# puzzle source
code day${day2}/p1.py
