#!/usr/bin/env python3

#requesting IP input from user
ipchk = input("Apply an IP address: ")

# checking for specific conditions for IP
if ipchk == "192.168.70.1":    #checking for specific IP: 192.168.70.1
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:     #if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk)
else:     #if data is NOT provided
   print("You did not provide input.")

