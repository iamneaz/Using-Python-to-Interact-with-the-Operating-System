# getting input from a text file and piping it to a python script
cat haiku.txt | python3 capitalize.py
# using redirection to get the previous result
python3 capitalize.py < haiku.txt