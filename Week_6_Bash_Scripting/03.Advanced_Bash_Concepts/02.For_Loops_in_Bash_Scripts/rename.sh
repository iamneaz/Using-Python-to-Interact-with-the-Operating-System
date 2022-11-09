for file in old_website/*.HTM; do 
    name=$(basename "$file" .HTM) # using double quotes on the file variable so that the code works if the file has spaces in its name
    mv "$file" "new_website/$name.html" #an echo in front of the MV command. This means that instead of actually renaming, our script we'll print the renaming that it plans to do.
done
