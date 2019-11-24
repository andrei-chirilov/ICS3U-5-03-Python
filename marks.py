#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program calculates the marks into percentages


def mark_finder(level):
    # This function will detirmine the mark into a percentage
    marks = {
        "4+": "97",
        "4": "91",
        "4-": "83",
        "3+": "78",
        "3": "75",
        "3-": "71",
        "2+": "68",
        "2": "65",
        "2-": "61",
        "1+": "58",
        "1": "55",
        "1-": "51",
        "0": "R"
    }

    # process
    if level in marks:
        return(marks[level])
    else:
        return False


def main():
    # This function takes user input and runs mark_finder()

    while True:
        level = input("Input the level: ")
        mark = mark_finder(level)
        if mark is False:
            print("Invalid input.")
        else:
            print("Your mark is " + mark + "%")
            break


if __name__ == "__main__":
    main()
