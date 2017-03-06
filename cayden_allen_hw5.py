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
            if pin.isnumeric() == True:
                print("Your PIN is incorrect")
                attempts += 1
            else:
                print("Invalid PIN character")
                attempts += 1
                if attempts == 3:
                    print("Your bank card is blocked")
                    return False
    
main()
