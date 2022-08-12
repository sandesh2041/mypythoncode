#!/usr/bin/env python3

count = 0
######## EXPLORE READ ########
#Create file object in read mode
configfile = open("vlanconfig.cfg", "r")

#Display file to the screen - .read()
print(configfile.read())

#close file
#configfile.close()


######## EXPLORE READLINES ########
#Re-create fe object to explore new method
#configfile = open("vlanconfig.cfg","r")

#Moving to start of the file
configfile.seek(0, 0)

#Make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

#Iterate through configlist
for x in configlist:
    count += 1
    print(x.strip())

#closing the file
configfile.close()

print("Number of lines:",count)



