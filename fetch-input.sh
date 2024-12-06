#!/bin/bash

# A 'cookie' file is necessary

year=`date "+%Y"`

day1=`date "+%e" | xargs`
day2=`date "+%d"`

cookie=`cat cookie`

curl -o inputs/day${day2}.txt "https://adventofcode.com/${year}/day/${day1}/input" --header "${cookie}"

# source files
code day${day2}/p1.py
