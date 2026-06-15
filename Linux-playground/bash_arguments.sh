#!/bin/bash
if [ "$#" -eq 0 ]; then
	echo "No arguments"
fi
if [ "$#" -gt 0 ]; then
	count=1
	for arg in $@; do	
		echo "Argument $count: $arg"
		count=$((count + 1))
	done
fi

