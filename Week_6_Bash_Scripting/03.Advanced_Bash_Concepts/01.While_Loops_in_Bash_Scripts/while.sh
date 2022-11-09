n=1
while [ $n -le 5 ]; do # $n is less than or equal to 5
    echo "Iteration number $n"
    ((n+=1)) # (()) is used to do arethmatic operations with the variables
done