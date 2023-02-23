#!/bin/bash


while true; do

read arg1 arg2 arg3

if [[ $arg1 == 'exit' ]]; then
	echo 'bye'; break; fi
	
case $arg2 in
	'+')let "ans = $arg1 + $arg3";;
	'-')let "ans = $arg1 - $arg3";;
	'*')let "ans = $arg1 * $arg3";;
	'/')let "ans = $arg1 / $arg3";;
	'%')let "ans = $arg1 % $arg3";;
	'**')let "ans = $arg1 ** $arg3";;
	*)echo 'error'; break
esac
echo $ans
done

