#!/bin/bash

name="x"
age=1

while [[ 0 -eq 0 ]]
do
	echo 'enter your name:'
	read name
	
	if [[ $name == "" ]]
	then
		break
	fi
	
	echo 'enter your age:'
	read age
	
	if [[ $age -eq 0 ]]
	then
		break
	fi
	
	if [[ $age -le 16 ]]
	then
		echo "$name, your group is child"
	elif [[ $age -ge 17 && $age -le 25 ]]
	then	
		echo "$name, your group is youth"
	else	
		echo "$name, your group is adult"
	fi
done

echo 'bye'
