while read -r fam ;
do

echo $fam
#cuts the .fa in each fam n sets a variable for name

name=$(echo "$fam" | cut -f 1 -d '.')

echo $name

#hmmbuild will build the HMM you must complete the alignment first on all families

hmmbuild family_HMM/$name.hmm Family_Alignment/$fam  

#insert the text file of the family name (family_list.txt)
done < $1
