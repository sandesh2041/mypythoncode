#!/usr/bin/env python3

#Creatin a list
my_list = ["192.168.0.5", 5060, "UP" ]

#Printing first item in the list
print("The first item in the list (IP): " + my_list[0])

#Printing second item in the list
print("The second item in the list (port): " + str(my_list[1]))

#Printing 3rd item in the list
print(f"The last item in the list (state): {my_list[2]}")

#Creating second list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#Displaying only IP addresses
print(f"IP addresses are: {iplist[3]} and {iplist[4]}")
