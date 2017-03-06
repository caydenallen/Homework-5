#!/usr/bin/env python3
import sys

# task: Verify users PIN. Block and exit program after 3 attempts


def verify(pin):
    if pin == '1234':
        return True
    else:
        return False


def main():
    attempts = 0
    while attempts < 4:
        pin = input("Please enter your PIN: ")
        if verify(pin):
            print("Your PIN is correct")
            return True
        else:
            print("Your PIN is incorrect")
            attempts += 1
        print("Your bank catd is blocked")
        return False
main()
