#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is game


def main():
    # This is elif_program

    # input
    number = int(input("Enter a integer: "))

    # process
    if number > 0:
        print("{0} is a positive number.".format(number))
    elif number < 0:
        print("{0} is a negative number.".format(number))
    else:
        print("0 is just zero!")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
