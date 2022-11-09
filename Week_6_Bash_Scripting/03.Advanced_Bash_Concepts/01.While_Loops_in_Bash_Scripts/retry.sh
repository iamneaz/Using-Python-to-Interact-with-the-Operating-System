n=0
command=$1 # accessing the first commandline argument in python we can do this by sys.argv[1]
while ! $command && [ $n -le 5 ]; do
    sleep $n # We are using sleep because if the command we're calling is failing due to CPU usage, network or resource exhaustion, it might make sense to wait a bit before trying again. So the more we try, the more we wait. We need to let our computer catch a breather and recover from whatever is making our command fail. 
    ((n=n+1))
    echo "Retry #$n"
done;