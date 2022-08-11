#!/usr/bin/env python3

def main():
    count = 1
    print('Finish the move title, "Monty Python\'s The Life of ..."')

    while count <= 3:
        response = input("Your answer: ")
        if response.lower() == 'brian':
            print("Correct!")
            break
        if count < 3:
            print("Sorry, try again!")
        else:
            print("Sorry, the answer was Brian.")
        count += 1
main()

