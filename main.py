#!/usr/bin/env python3

from colorama import Fore, Back, Style
import readchar
import argparse
import random
import string
from time import time
from collections import namedtuple

Input = namedtuple('Input', ['requested', 'received', 'duration'])

def test(stop_key, max_iteration, max_time_seconds):

    # Ask for all the entries and put them in a list
    pressed_keys = [] # empty list to start with
    list_input = []
    iteration = 0
    dur = 0;

    t_global_start = time()

    while True:

        if max_time_seconds == 0:
            pass
        elif dur >= max_time_seconds:
            print('\nTEST ENDED! You achieved the time limit\n')
            break

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

        dur += input_duration

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

    parser = argparse.ArgumentParser(description='PSR - TP1')
    # parser.add_argument('--h', action='store_true', help='Print help message')
    parser.add_argument('--mv', type=int, help='Maximum number of iterations')
    parser.add_argument('--utm', type=int, help='Number of seconds for the test', default=0)
    args = vars(parser.parse_args())
    print(args)

    print("Starting Test")

    max_iteration = args['mv']
    max_time_seconds = args['utm']


    test(' ', max_iteration, max_time_seconds)

if __name__ == "__main__":
    main()