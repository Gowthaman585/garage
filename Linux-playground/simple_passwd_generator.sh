#!/bin/bash
echo "Simple password generator"
echo "Enter the length password to generate :"
read PASS_LEN
for p in $(seq 1);
do
	openssl rand -base64 48 | cut -c 1-$PASS_LEN
done
