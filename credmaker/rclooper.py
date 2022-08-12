#!/usr/bin/env python3
"""Using the csv library to work with CSV data"""

#standard library import
import csv

#opne our csv data
with open("csv_users.txt","r") as csvfile:

    #counter to create unique filename
    i = 0
    #loop to open file line by line
    for row in csv.reader(csvfile):
        i = i + 1
        filename = f"admin.rc{i}"

        #open file to write the content
        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

print("admin.rc files created!")

