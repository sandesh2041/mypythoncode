#!/usr/bin/env python3
"""For - Looping across a file opened with 'with'
        while also being gentle on memory consumption."""

#open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #loop across the lines in the file
    for svr in dnsfile:
        print(svr, end="")

