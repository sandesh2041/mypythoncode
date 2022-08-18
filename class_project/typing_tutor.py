#!/usr/bin/env python3
""" Python Project | Sam Maskey
    This project will provide your tying speed and accuracy """

# TODO: Need condition for speed = 0
# TODO: Need condition for no input entered

import json
import time
import os
import random
import requests


def get_file_string():
    filename = 'strings_easy.txt'
    print(f"Getting string from '{filename}'")
    time.sleep(2)
    file_open = open(filename).read()
    strings = file_open.split('\n')
    string = random.choice(strings)
    return string


def get_api_string():
    url = "https://type.fit/api/quotes"
    print(f"Getting quote from '{url}'")
    time.sleep(2)
    response = requests.request("GET", url).text
    converted_response = json.loads(response)
    i = random.randint(1, len(converted_response))
    string = converted_response[i]['text']
    return string


# Calculating Character Accuracy
def char_accuracy_calc(text_displayed, text_typed):
    count = 0
    for index, character in enumerate(text_typed):
        try:
            if text_displayed[index] == character:
                count += 1
        except:
            pass

    accuracy = round((count / len(text_displayed) * 100), 2)
    return accuracy


# Calculating Word Accuracy
def word_accuracy_calc(text_displayed, text_typed):
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


def main():
    minutes = 0
    text_displayed = "Default string"

    print("Are you ready to test you tying skills!!!")
    option = input("Press 'y' to start & 'n' to exit > ")

    if option == 'y':
        while option == 'y':
            os.system('clear')  # Not working in Pycharm, WHY?
            print("===========================")
            print("Where you want the text from:")
            print("1. Random string from file")
            print("2. Random quote from api call")
            print("===========================")
            # print("3. Exit")
            selection = input("Enter your selection (1 or 2): ")
            if selection == '1':
                text_displayed = get_file_string()
            elif selection == '2':
                text_displayed = get_api_string()
            # elif selection == 3:
            #    break

            print(f"***** {text_displayed} *****")
            start_time = time.time()

            print("Retype the above string inside *** ")
            text_typed = input(" > ")

            # Calculating Speed
            end_time = time.time()

            time_taken = int(end_time - start_time)
            if time_taken >= 60:
                # convert into minutes
                minutes = int(time_taken / 60)
                seconds = int(time_taken % 60)
            else:
                seconds = time_taken

            num_of_words = len(text_displayed.split())
            speed = round((num_of_words / time_taken * 60), 2)
            char_accuracy = char_accuracy_calc(text_displayed, text_typed)
            word_accuracy = word_accuracy_calc(text_displayed, text_typed)

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
            option = input("Press 'y' to start / 'n' to exit > ")

    if option == 'n':
        os.system('clear')
        print("Goodbye!!!")


if __name__ == "__main__":
    main()
