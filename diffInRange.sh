#!/bin/bash

sed -n "$2,$3p" $1 > $1.txt
sed -n "$5,$6p" $4 > $4.txt

diff -u --ignore-all-space --ignore-blank-lines	 $4.txt $1.txt

rm $4.txt
rm $1.txt


# #!/bin/bash

# sed -n "$2,$3p" $1 > old.txt
# sed -n "$5,$6p" $4 > new.txt

# diff -u --ignore-all-space --ignore-blank-lines	 new.txt old.txt

# rm old.txt
# rm new.txt