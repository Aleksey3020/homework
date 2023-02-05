#!/bin/bash

PS3="Do you want to install python? "
echo
select answers in Yes No
do
case $answers in
"Yes") echo "You chose to install python"
break ;;
"No") echo "Go away close the door"
break ;;
esac
done