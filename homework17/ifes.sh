#!/bin/bash

if (( $1 > 0  ))
then
echo "$1 is pozitive"
else
echo "$1 is negative"
fi


if [ -e $2 ]
then
echo "$2 faile exists"
else
echo "$2 faile not exists"
fi