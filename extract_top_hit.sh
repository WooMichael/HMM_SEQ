grep -A 1 "#------------------- " $1/* | grep --invert-match "#" > $2/$3_top_only.txt	
