#!/bin/bash

printf 'Enter the number: '
read number1 number2

if (( $number1 > 15 && $number1 < 45 ))
then
echo "the number $number1 is in the range from 15 to 45"
else
echo "the number $number1 is not in the range from 15 to 45"
fi

if (( $number2 < -1 ||  $number2 == 45 ))
then
echo "the number $number2 matches one of the conditions: number<-1 or number=45"
else
echo "the number $number2 does not match any of the condition"
fi