> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3 | cut -d '/' -f 3);
echo $directory
for file in $files;do
    if test -e ../data/$file; then
        "baka" > oldFiles.txt;
    else 
        realpath=$(readlink -f ../data/$file);
        echo $realpath >> oldFiles.txt;
    fi
done

> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3 | cut -d '/' -f 3);
for file in $files;do
    if test -e ../data/$file; then
        realpath=$(readlink -f ../data/$file);
        echo $realpath >> oldFiles.txt;
    fi
done


