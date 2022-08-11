#!/usr/bin/env python3

def main():
    #Asking user input for numeric score
    score = int(input("Enter your score: "))

    if score > 100:
        print("Score cannot be more than 100, YOU LIAR!!!")
    elif score < 0:
        print("You suck more than I think!!!")
    else:
        if score >= 90:
            print("Excellect work. You got 'A'")
        elif score >= 80:
            print("Good job. You got 'B' but you can still make it better")
        elif score>=70:
            print("I know you trying. Keep pushing yourself. You got 'C'")
        elif score>=60:
            print("You need to pick it up homie! You in that borderline. You got 'D'")
        else:
            print("Get your shit together rookie! You messed up. You got 'F'")

main()
