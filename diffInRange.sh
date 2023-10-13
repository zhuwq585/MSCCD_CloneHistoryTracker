#!/bin/bash

sed -n "$2,$3p" $1 > temp1.txt
sed -n "$5,$6p" $4 > temp2.txt

diff -u temp1.txt temp2.txt

rm temp1.txt
rm temp2.txt