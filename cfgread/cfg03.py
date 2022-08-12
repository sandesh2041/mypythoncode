#!/usr/bin/env python3

#Asking for user input
filename = input("Enter the name of the file to read:")

## create file object in "r"ead mode
with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)


