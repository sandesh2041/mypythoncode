#!/usr/bin/env python3
"""This program combines the list and return the favorite food"""

#Making 3 list of foods
foodList = ["Pizza", "Pasta"]
foodList1 = ["MoMo", "Chicken Tikka Masala"]
foodList2 = ["Bulgogi", "Galbi"]

#Adding list of food using append
foodList.append(foodList1)
#Adding list of food using extend
foodList.extend(foodList2)

#Printing list of foods
print("List of foods:")
print(foodList)

#Printing my favorite food
print("\nMy favorite food: " + foodList[2][0])


#Creating dictory
superheroes = {
        "Thor" : {
            "weapon" : "hammer",
            "species" : "god",
            "fly" : True
            },
        "Captain American": {
            "weapon" : "shield",
            "species" : "human",
            "fly" : False
            },
        "Vision": {
            "weapon" : "mind stone",
            "species" : "AI",
            "fly" : True
            }
        }

#Printing all the keys
print("\nList of keys:")
print(superheroes.keys())

#Printing all the values
print("\nList of values:")
print(superheroes.values())
