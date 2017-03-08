#!/usr/bin/env python3
import sys

# task: Verify users PIN. Block and exit program after 3 attempts

def verify(pin):
    """
    Verifies user input against users pin and returns true or false
    Usage:
        (####) numbers only
    """
    if pin == '1234':
        return True
    else:
        return False


def GetInput():
    """
    Checks if PIN was correct or not. Loops through until PIN is correct
    or if the user has 3 failed attempts.
    Args:
        PIN - Personal Identification Number
    Return:
        Whether or not the PIN is correct. If user has 3 failed attempts
        program will return "your card has been blocked" error and exit
    """
    attempts = 0
    while attempts < 4:
        pin = input("Please enter your PIN: ")
        if verify(pin):
            print("Your PIN is correct")
            return True
        else:
            if len(pin) != 4:
                print("Invalid PIN length. Correct format is: <9876>")
                attempts += 1
                if attempts == 3:
                    print("Your bank card is blocked")
                    return False
            elif pin.isnumeric() == True:
                print("Your PIN is incorrect")
                attempts += 1
                if attempts == 3:
                    print("Your bank card is blocked")
                    return False
            else:
                print("Invalid PIN character. Correct format is: <9876>")
                attempts += 1
                if attempts == 3:
                    print("Your bank card is blocked")
                    return False

def main():
    if __name__ == '__main__':
        GetInput()
        exit(0)


main()
