#!/usr/bin/env python3

#Requesting IP input from user
ipchk = input("Apply an IP address: ")

# Checking if ipchk exists
if ipchk: #input provided
   print("Looks like the IP address was set: " + ipchk)
else: #input not provided
    print("You did not provide input")


