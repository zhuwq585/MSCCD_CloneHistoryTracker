#!/bin/bash

sed -n "$2,$3p" $1 > old.txt
sed -n "$5,$6p" $4 > new.txt

diff -u --ignore-all-space --ignore-blank-lines	 old.txt new.txt

rm old.txt
rm new.txt