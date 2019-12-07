# Input file has 3 columns separated by white space (space or tab characters only).
while read -r name count; do
  # Only print the last name (second column)
  echo "$name"
  ~/Development/Clustal/clustal-omega-1.2.4/src/clustalo -i "f/$name" -o "family/msa_$name"
done < family_count
