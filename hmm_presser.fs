while read -r fam;
do  
#echo $fam
#insert the fam.txt file
hmmpress family_individuals_pressed/$fam/$fam
done < $1
