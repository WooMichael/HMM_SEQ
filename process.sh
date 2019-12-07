for f in *.txt
do
	echo "Processing $f"
	name=${f%.*}
	grep -A 1 "# -------------------" $f | grep "msa" | tr -s ' ' | cut -d ' ' -f 1,3 > $name.cut.txt
done
