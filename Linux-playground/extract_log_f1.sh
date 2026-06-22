#!/bin/bash
if test $# -eq 0; then
	echo -e "No arguments provided\nUSAGE: ./<script-name> Accepted/Failed"
	exit 1;
elif test $# -gt 1; then
	echo -e "Too many arguments\nFAILED!"
fi
arg="$1"
if test "$arg" = "Failed" || test "$arg" = "Accepted"; then
	grep "$arg" auth.log
else 
	echo "Invalid arguments"
fi
