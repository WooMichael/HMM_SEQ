while read -r fam query ;
do
#echo $fam $query
#insert the all query text
hmmscan --noali --tblout $query.txt family_individuals_pressed/$fam/$fam $2/$query.fa
done < $1
