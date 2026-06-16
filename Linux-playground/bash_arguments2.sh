#!/bin/bash

# This script below are wriiten when a task is taken
# in LABEX lab's.
# ****************************************************
#
# Define arrays for each cargo bay's inventory
# To declare an array in bash we need to use ()
#
# ****************************************************
# SYNTAX >>>>> VAR_NAME=()
# ****************************************************
forward_bay=()
midship_bay=()
aft_bay=()
# ****************************************************
# 
# Defininig variables for each array
# LABEX Description:
# each array need to have exactly three elements in it.
# 
# ****************************************************

forward_bay+=("Space Suits")
forward_bay+=("oxygen Tanks")
forward_bay+=("Repair Kits")
midship_bay+=("Food Supplies")
midship_bay+=("Water Containers")
midship_bay+=("Medical Equipment")
aft_bay+=("Spare Parts")
aft_bay+=("Fuel Cells")
aft_bay+=("Scientific Instruments")

# ****************************************************

# Check if an argument is provided
if [ $# -eq 0 ]; then
    # Your code here
    echo "Please specify a cargo bay: Forward,midship or aft"
    exit 1
fi

# Totally Three arguments are allowed:
# forward, midship, aft.
# Display inventory based on the argument

if [ "$1" = "forward" ]; then
    count=1
    for inv in "${forward_bay[@]}"; do
        echo "${count}. ${inv}"
        count=$((count+1))
    done

elif [ "$1" = "midship" ]; then
    count=1
    for inv in "${midship_bay[@]}"; do
    echo "${count}. ${inv}"
    count=$((count+1))
    done

elif [ "$1" = "aft" ]; then
    count=1
    for inv in "${aft_bay[@]}"; do
    echo "${count}. ${inv}"
    count=$((count+1))
    done

# If invalid argument passed:
else
    echo "Invalid cargo bay. choose forward, midship or aft_bay." 
    exit 1
fi

