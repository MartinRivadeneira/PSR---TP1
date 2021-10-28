#!/usr/bin/env python3

from colorama import Fore, Back, Style
import readchar
import argparse
import random
import string
from time import time
from collections import namedtuple

Input = namedtuple('Input', ['requested', 'received', 'duration'])

def printAllCharsUpTo(stop_char):

    print('I dont know how to do it yet')

    print('Printing all the values up to stop_char ' + str(stop_char))
    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))

def test(stop_key, max_iteration):

    # Ask for all the entries and put them in a list
    pressed_keys = [] # empty list to start with
    list_input = []
    iteration = 0

    t_global_start = time()

    while True:

        t_local_start = time()
        letter = random.choice(string.ascii_lowercase)
        print('Type ' + Fore.LIGHTBLUE_EX + str(letter) + Style.RESET_ALL + ' or space to stop: ')
        pressed_key = readchar.readchar()
        iteration += 1

        if pressed_key == stop_key:
            print('\nTEST ENDED! You pressed space.\n')
            break
        else:
            pressed_keys.append(pressed_key)

            if pressed_key == letter:
                print('You pressed ' + Fore.GREEN + str(pressed_key) + Style.RESET_ALL + ' so your answer is CORRECT!')
            else:
                print('You pressed ' + Fore.RED + str(pressed_key) + Style.RESET_ALL + ' so your answer is INCORRECT!')

        if iteration == max_iteration:
            print('\nTEST ENDED! You achieved the maximum iteration\n')
            break

        t_local_end = time()

        input_duration = t_local_end - t_local_start

        Tuple = Input(requested = letter, received = pressed_key, duration = input_duration)
        list_input.append(Tuple)

    t_global_end = time()
    test_duration = t_global_end - t_global_start

    print('The keys you pressed are: ' + str(pressed_keys))

    print('\nList of inputs is:\n')
    for i in list_input:
        print(str(i))

    print('\nTest duration: ' + str(test_duration) + 's')

def main():

    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--maximum_number', type=int, help='Maximum number to search for primes.')
    parser.add_argument('--verbose', action='store_true', help='Print stuff to the screen or not')
    args = vars(parser.parse_args())
    print(args)

    print("Starting to compute prime numbers up to " + str(args['maximum_number'] - 1))

    max_iteration = args['maximum_number']
    test(' ', max_iteration)

if __name__ == "__main__":
    main()