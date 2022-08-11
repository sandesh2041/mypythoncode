#!/usr/bin/env python3
""" For - Looping across range() to generate n UUIDs"""

#standard library import that allow us to generate UUIDs
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

#range is required because an int cannot be looped
for rando in range(howmany):
    print(uuid.uuid4())

