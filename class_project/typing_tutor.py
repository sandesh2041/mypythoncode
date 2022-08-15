#!/usr/bin/env python3
""" Python Project | Sam Maskey 
    This project will provide your tying speed and accuracy """

import time

def main():

    textDisplayed  = "This is a random string to test."
    print(textDisplayed)
    
    starttime = time.time()
    
    print("Retype the above string: ")
    textTyped = input(" > ")
    print(textTyped)
    
    endtime = time.time()
    
    timetaken = int(endtime - starttime)
    if(timetaken >= 60):
        #convert into minutes

    print(f"Total Time Taken: {timetaken}secs")

main()
