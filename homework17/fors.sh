#!/bin/bash

for  i in {11..1}
do
if (( $i % 2 == 0 ))
then 
echo $i
fi
done