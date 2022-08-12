#!/usr/bin/env python3
"""Return the number of failed and successful login attemps"""

#Counter for failed and successful logins
loginfail = 0
loginsuccess = 0
ip = "" 

#opening file to read
with open("/home/student/mypythoncode/attemptlogin/keystone.common.wsgi") as kfile:
    
    #loop over the file
    for line in kfile:

        #checking condition for failed login
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            ip = line.split(" ")[-1]
        elif "-] Authorization failed" in line:
            loginsuccess += 1

print("The number of failed login attempts is", loginfail)
print("Failed login ip addresses is", ip, end="")
print("The number of successful login attempts is", loginsuccess)

