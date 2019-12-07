while read -r longfam target; do
  fam=${longfam#*_}
  echo "Processing $fam $target..."
  # nhmmer --noali --tblout $target.top.txt $2/$target.fa 
done < $1
