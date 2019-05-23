#!/bin/bash
if [ -z $1 ]; then
	echo "Please provide an epoch timestamp in ms to convert to a date"
	exit 1
fi
date -d @$( echo $1 / 1000 | bc)
