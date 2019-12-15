while read -r name ; do
echo "Processing: $name "
Clustal_Omega/clustalo.exe -i Family/$name -o Family_Alignment/$name 
echo "Alignment Complete : $name"
done < $1
ls Family_Alignment > s1.txt
grep -v -f family_list.txt s1.txt > one_seq_names.txt
rm s1.txt
