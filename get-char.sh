#!/bin/zsh

read input
index="$1"

echo "$input" | head -c $1 | tail -c 1
echo
