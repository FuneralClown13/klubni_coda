#!/bin/bash


gcs ()
{
	if [[ $1 -gt $2 ]]; then
		arg1=$1
		arg2=$2
	else
		arg1=$2
		arg2=$1
	fi
	
	
	while true; do
	
	let "x = $arg1 % $arg2"
	
	if [[ x -eq 0 ]]; then
		echo "GCD is $arg2"; break
	fi
	
	arg1=$arg2	
	arg2=$x
	
	done

}


while true; do
read arg1 arg2

if [[ $arg1 == '' ]]; then
	echo 'bye'; break
fi

gcs $arg1 $arg2
done
