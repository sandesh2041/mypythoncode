#!/usr/bin/env python3
"""Parse keystone.common.wsgi and return number of failed login attemps"""

#counter for fail
loginfail = 0

#open file for reading
keystone_file = open("/home/student/mypythoncode/attemptlogin/keystone.common.wsgi","r")

#making the list of lines from the file
keystone_file_lines = keystone_file.readlines()

#loop over list of lines
for line in keystone_file_lines:
    #checking for the failed pattern
    if "- - - - -] Authorization failed" in line:
        loginfail += 1

print("The number of failed log in attemps is", loginfail)

#closing the file
keystone_file.close()
