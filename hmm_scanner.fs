







#we want to first get a list of the queries we have to make

ls $1 > s1.txt

while read -r query ;
do 
echo $query

#run this query into the database that we made

name=$(echo "$query" | cut -f 1 -d '.')
mkdir output

#make sure you have an output placed so I going to use a generic one for all intensive purposes
#placed the path to your DB
#placed the path to your query **we will use a $1 so when we bash we can do it for all of the sequence queries we want to do without changing the code
#make sure to have a directory created already

hmmscan --noali --tblout output/$name.txt FamilyDB $1/$query
 
done < s1.txt
#removes temp text file
rm s1.txt   
