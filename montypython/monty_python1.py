#!/usr/bin/env python3

def main():
    count = 1
    print('Finish the move title, "Monty Python\'s The Life of ..."')

    while count <= 3:
        response = input("Your answer: ")
        if response.capitalize() == 'Brian':
            print("Correct!")
            break
        elif response.capitalize() == 'Shrubbery':
            print("you gave the super secret answer!")
            break
        if count < 3:
            print("Sorry, try again!")
        else:
            print("Sorry, the answer was Brian.")
        count += 1
main()

