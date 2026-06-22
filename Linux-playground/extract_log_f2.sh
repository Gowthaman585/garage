#!/bin/bash
#Detecting the presence of log source.
if test ! -f "auth.log" ; then
       echo "No log source found"
       exit 1
else
	echo -e "source founded!\n==================="
fi
echo -e "testing : arguments presence"
#Restricting unwanted arguments to be exit.
if test $# -eq 0; then
	echo -e "No arguments founded\nUSAGE: ./<filename> Accepted/Failed"
	exit 1
fi
if test $# -gt 1; then
	echo -e "too many arguments\nFAILED!"
	exit 1
fi
# only valid arguments are allowed here to process.
arg=$1
if test "$arg" = "Failed" || test "$arg" = "Accepted" ; then
	while read -r line ; do
		stat=$( echo "$line" | cut -d " " -f 6)
		if test "$stat" = "$arg" ; then
			echo "$line"
		fi
	done < auth.log
else
	echo "Invalid argument"
fi
