#!/bin/bash

sum=0

while read line || [[ -n $line ]]
do
    numbers=`echo $line | sed -E 's/[^0-9]//g'`

    a=${numbers: 0:1}
    b=${numbers: -1:1}

    sum=$[$sum + $a$b]

done < inputs/day-1.txt

echo $sum
