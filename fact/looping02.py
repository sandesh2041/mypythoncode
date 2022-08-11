#!/usr/bin/env python3
"""For - Using a file's lines as a source for the for-loop"""

#open file in read mode
dnsfile = open("dnsservers.txt", "r")

#create list of lines
dnslist = dnsfile.readlines()

#loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")

#close the file
dnsfile.close()


