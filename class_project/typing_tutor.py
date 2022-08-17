#!/usr/bin/env python3
""" Python Project | Sam Maskey 
    This project will provide your tying speed and accuracy """

#TODO: Need condition for speed = 0
#TODO: Need condition for no input entered

import time

def main():

    mins = 0
    seconds = 0

    textDisplayed  = "This is a random string to test."
    print(textDisplayed)
    
    num_of_words = len(textDisplayed.split())
    print(num_of_words)

    starttime = time.time()
    
    print("Retype the above string: ")
    textTyped = input(" > ")

    endtime = time.time()
    
    timetaken = int(endtime - starttime)
    if(timetaken >= 60):
        #convert into minutes
        mins = int(timetaken / 60)
        seconds = int(timetaken % 60)
    else:
        seconds = timetaken

    speed = round((num_of_words / timetaken * 60), 2) 

    print(f"Total Time Taken: {mins}mins {seconds}secs")
    print(f"Your Speed is: {speed} wpm")

main()
