ls $1 > s1.txt
while read -r name ;
do
#if you want to save the outout of the grep use the greater than symbol and the name of the file you want to place it in

grep -A 1 "#-------------------" $1/$name | tr -s ' ' |cut -d ' ' -f 1,3 | sed -n '1!p'


done < s1.txt
rm s1.txt
