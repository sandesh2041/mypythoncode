#!/usr/bin/env python3
""" Python Project | Sam Maskey
    This project will provide your tying speed and accuracy """

import json
import time
import os
import random
import requests
import matplotlib.pyplot as plt
import numpy as np


def get_file_string():
    """Function extracting single random string from file"""
    filename = 'strings_easy.txt'
    print(f"Getting string from '{filename}'")
    time.sleep(1)
    os.system('clear')
    with open(filename, encoding="utf-8") as file_open:
        file_read = file_open.read()
        strings = file_read.split('\n')
        string = random.choice(strings)
        return string


def get_api_string():
    """Function extracting single random quote from API"""
    url = "http://quotes.stormconsultancy.co.uk/quotes.json"
    print(f"Getting quote from '{url}'")
    time.sleep(1)
    os.system('clear')
    response = requests.get(url)
    converted_response = json.loads(response.text)
    i = random.randint(1, len(converted_response))
    string = converted_response[i]['quote']
    return string


def char_accuracy_calc(text_displayed, text_typed):
    """Function calculating character accuracy"""
    count = 0
    for index, character in enumerate(text_typed):
        try:
            if text_displayed[index] == character:
                count += 1
        except:
            pass

    accuracy = round((count / len(text_displayed) * 100), 2)
    return accuracy


def word_accuracy_calc(text_displayed, text_typed):
    """Function calculating word accuracy"""
    count = 0
    words_displayed = text_displayed.split()
    words_typed = text_typed.split()

    for index, word in enumerate(words_typed):
        try:
            if words_displayed[index] == word:
                count += 1
        except:
            pass

    accuracy = round((count / len(words_displayed) * 100), 2)
    return accuracy


def chart(char_acc, word_acc, speed):
    """Function creating bar chart"""
    length = len(char_acc)
    # Label Location
    xaxis = np.arange(length) + 1
    # Width of the bar
    width = 0.35  # the width of the bars

    fig, axes = plt.subplots()
    rects1 = axes.bar(xaxis - width / 2, char_acc, width, label='Character Accuracy')
    rects2 = axes.bar(xaxis + width / 2, word_acc, width, label='Word Accuracy')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    axes.set_ylabel('Accuracy in %')
    axes.set_title('Typing Speed and Accuracy')
    axes.set_xticks(xaxis)
    axes.legend()

    axes.bar_label(rects1, padding=3)
    axes.bar_label(rects2, padding=3)

    axes2 = axes.twinx()
    axes2.set_ylabel('Speed in wpm')
    axes2.plot(xaxis, speed, 'o-', color='crimson', linewidth=2, label='Speed')
    axes2.legend(loc="upper left")
    for i in range(len(xaxis)):
        axes2.text(xaxis[i], speed[i], speed[i], size=10)

    fig.tight_layout()

    plt.savefig("/home/student/static/chart.png")


def main():
    """Function main method"""
    minutes = 0
    text_displayed = "Default string"
    type_speed = []
    char_acc = []
    word_acc = []

    print("Are you ready to test you tying skills!!!")
    option = input("Press 's' to start or 'e' to exit > ")

    while option.lower() != 's' or option.lower() != 'e':
        if option.lower() == 's':
            while option.lower() == 's':
                os.system('clear')
                print("===========================")
                print("Where you want the text from:")
                print("1. Random string from file")
                print("2. Random quote from api call")
                print("===========================")

                selection = input("Enter your selection (1 or 2): ")
                while selection != '1' or selection != '2':
                    if selection == '1':
                        text_displayed = get_file_string()
                        break
                    if selection == '2':
                        text_displayed = get_api_string()
                        break
                    else:
                        print("Invalid selection!!!! PLease enter valid input.")
                        selection = input("Enter your selection (1 or 2): ")
                os.system('clear')
                print(f"***** {text_displayed} *****")
                print('\n')

                # Capture typing start time
                start_time = time.time()

                print("Retype the above string inside *** ")
                text_typed = input(" > ")

                # Capture tying end time
                end_time = time.time()

                # Total time taken to type
                time_taken = int(end_time - start_time)
                if time_taken >= 60:
                    # convert into minutes
                    minutes = int(time_taken / 60)
                    seconds = int(time_taken % 60)
                else:
                    seconds = time_taken

                num_of_words = len(text_displayed.split())

                # Typing speed calculation
                speed = round((num_of_words / time_taken * 60), 2)

                # Calling function to calculate accuracy
                char_accuracy = char_accuracy_calc(text_displayed, text_typed)
                word_accuracy = word_accuracy_calc(text_displayed, text_typed)

                char_acc.insert(len(char_acc), char_accuracy)
                word_acc.insert(len(word_acc), word_accuracy)
                type_speed.insert(len(type_speed), speed)

                print("===========================")
                if time_taken >= 60:
                    print(f"Total Time Taken: {minutes} mins {seconds} secs")
                else:
                    print(f"Total Time Taken: {seconds} secs")
                print(f"Your Speed: {speed} wpm")
                print(f"Accuracy per character: {char_accuracy}%")
                print(f"Accuracy per word: {word_accuracy}%")
                print("===========================")

                print("Do you want to try again?")
                option = input("Press 's' to start or 'e' to exit > ")

        elif option.lower() == 'e':
            chart(char_acc, word_acc, type_speed)
            print("Goodbye!!!")
            break

        else:
            print("Invalid selection!!!! PLease enter valid input.")
            option = input("Press 's' to start or 'e' to exit > ")


if __name__ == "__main__":
    main()
