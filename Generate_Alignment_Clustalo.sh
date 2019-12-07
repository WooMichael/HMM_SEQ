while read -r name ; do
#echo $name 
Clustal_Omega/clustalo.exe -i Family/$name -o Family_Alignment/$name 
done < $1
ls Family_Alignment > s1.txt
diff family_list.txt st.txt > one_seq_names.txt
rm s1.txt
