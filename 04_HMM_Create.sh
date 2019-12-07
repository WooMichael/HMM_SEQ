#create hmm off of pre-aligned multiple sequences
while read -r name count; do

echo "name"

hmmbuild "hmmFam/$name.hmm" "family/$name"
done < genus_count
