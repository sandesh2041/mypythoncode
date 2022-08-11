#!/usr/bin/env python3

def main():
    #Creating list of dictionary
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        #print(farm)
        print(farm.get("name", "Unknown Farm"), end="\n")

        for agri in farm.get("agriculture"):
            print(" -", agri)

if __name__ == "__main__":
    main()

