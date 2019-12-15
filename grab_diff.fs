while read -r name ; do
grep $name $2
done < $1
