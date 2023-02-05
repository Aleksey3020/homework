#!/bin/bash

printf 'Enter symbol: '
read symbol
case $symbol in
[[:lower:]]) echo "lower case letter" ;;
[[:upper:]]) echo "THE LETTER IN UPPER CASE" ;;
[0-9]) echo "Number" ;;
*) echo "Special symbol" ;;
esac