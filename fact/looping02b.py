#!/usr/bin/env python3
"""For - Looping across a file opened with 'with'"""

#open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #create list of lines
    dnslist = dnsfile.readlines()

    #loop over the lines
    for svr in dnslist:
        #print and end without a new line
        print(svr, end="")

#no need to close the file

