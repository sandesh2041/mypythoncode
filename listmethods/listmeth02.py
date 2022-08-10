#!usr/bin/env python3

#Creating a list of fruits
list1 = ["orange", "banana", "grapes", "apple"]
print(list1)

#Insert a new fruit at the end of list using insert
list1.insert(len(list1), "strawberry")
#Displaying list after adding new item
print(list1)

#Removing first item in the list which is equal to given value
list1.remove("grapes")
#Displaying list after removing first item
print(list1)

#Removing last item in the list
print("Last item popped is: " + list1.pop())
#Displaying after popping second item in the list
print(list1)

#Counting the number of times specified item appears in list
print("Orange appears : " + str(list1.count("orange")) + " times")

#Sorting the list
print(sorted(list1))

