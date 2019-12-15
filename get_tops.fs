grep -A 1 "# -------------------" $1 | grep "msa" | tr -s ' ' | cut -d ' ' -f 1,3

