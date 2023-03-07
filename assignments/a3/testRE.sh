#!/bin/bash
# Test the regular expression with `re-congnizer.py` script and using regular expressions from `q1.txt` file

# re-congnizer.py script is a script that runs in interactive mode, so use `echo` to send the input to the script

# `q1-inp.txt` contains three lines each line is a regular expression
# `test<1-3>.txt` contains the test strings for each regular expression

# for each regular expression in `q1-inp.txt` file
# run the python script with the regular expression and the test string
# and exit the script by sending `q` to the script
for i in {1..3}
do
    # run python script
    python3 re-recongnizer.py
    # wait for the script to start
    sleep 2
    # send the regular expression to the script
    echo -e "$(cat q1-inp.txt | head -n $i | tail -n 1)\n"
    # send the test string to the script
    for j in {1..5}
    do
        echo -e "$(cat test$i.txt | head -n $j | tail -n 1)\n"
    done
    # exit the script
    echo "q\n"
done