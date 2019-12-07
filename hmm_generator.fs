while read -r fam indiv;
do
 #family_individuals/$fam/$indiv
#use all_family.txt file
#hmmbuild --cpu 7 family_individuals_db/$fam/$indiv.hmm family_individuals/$fam/$indiv
#echo $fam $indiv.hmm
#create db by attaching them to all strings #use all fam.txt file
cat family_individuals_db/$fam/* > family_individuals_pressed/$fam/$fam
done < $1 







