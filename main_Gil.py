#!/usr/bin/env python3

# $ pip install interruptingcow
import json
from pprint import pprint

from colorama import Fore, Back, Style
import readchar
import argparse
import random
import string
from collections import namedtuple
from time import time, ctime, sleep
from interruptingcow import timeout

Input = namedtuple('Input', ['requested', 'received', 'duration'])


def test(stop_key, max_iteration, max_time_seconds):

    # Initialize variables

    miss_duration = []
    hit_duration = []
    Total_inputs = {}
    number_of_hits = 0
    number_of_types = 0
    pressed_keys = []
    list_input = []
    iteration = 0

    t_global_start = time()

    # Max Value Mode:

    if max_time_seconds == 0:
        while True:
            letter = random.choice(string.ascii_lowercase)
            print('Type ' + Fore.LIGHTBLUE_EX + str(letter) + Style.RESET_ALL + ' or space to stop: ')

            # Starting clocks
            test_start = ctime()
            t_local_start = time()

            pressed_key = readchar.readchar()
            iteration += 1

            # Stop program by space
            if pressed_key == stop_key:
                print('\nTEST ENDED! You pressed space.\n')
                test_end = ctime()
                break

            else:
                pressed_keys.append(pressed_key)
                t_local_end = time()
                test_end = ctime()

                # Correct answer
                if pressed_key == letter:
                    print('You pressed ' + Fore.GREEN + str(
                        pressed_key) + Style.RESET_ALL + ' so your answer is CORRECT!')
                    number_of_hits += 1
                    number_of_types += 1
                    hit_duration.append(
                        t_local_end - t_local_start)

                # Wrong answer
                else:
                    print('You pressed ' + Fore.RED + str(
                        pressed_key) + Style.RESET_ALL + ' so your answer is INCORRECT!')
                    number_of_types += 1
                    miss_duration.append(
                        t_local_end - t_local_start)

            # Ending clocks
            t_local_end = time()
            input_duration = t_local_end - t_local_start

            # Define tuple for input data
            Tuple = Input(str(letter), str(pressed_key), str(input_duration))
            list_input.append(Tuple)

            # Stop program by Max Value
            if iteration == max_iteration:
                print('\nTEST ENDED! You achieved the maximum iteration\n')
                break

    # Max Time Mode
    else:
        try:
            with timeout(max_time_seconds, exception=RuntimeError):
                while True:
                    letter = random.choice(string.ascii_lowercase)
                    print('Type ' + Fore.LIGHTBLUE_EX + str(letter) + Style.RESET_ALL + ' or space to stop: ')

                    # Starting clocks
                    test_start = ctime()
                    t_local_start = time()

                    pressed_key = readchar.readchar()
                    iteration += 1

                    # Stop program by space
                    if pressed_key == stop_key:
                        print('\nTEST ENDED! You pressed space.\n')
                        test_end = ctime()
                        break
                    else:
                        pressed_keys.append(pressed_key)
                        t_local_end = time()
                        test_end = ctime()

                        # Correct answer
                        if pressed_key == letter:
                            print('You pressed ' + Fore.GREEN + str(pressed_key) + Style.RESET_ALL + ' so your answer is CORRECT!')
                            number_of_hits += 1
                            number_of_types += 1
                            hit_duration.append(t_local_end - t_local_start)

                        # Wrong answer
                        else:
                            print('You pressed ' + Fore.RED + str(pressed_key) + Style.RESET_ALL + ' so your answer is INCORRECT!')
                            number_of_types += 1
                            miss_duration.append(t_local_end - t_local_start)

                    # Ending clocks
                    t_local_end = time()
                    input_duration = t_local_end - t_local_start

                    # Define tuple for input data
                    Tuple = Input(str(letter), str(pressed_key), str(input_duration))
                    list_input.append(Tuple)

        # Stop program by Max Time
        except RuntimeError:
            print('\nTEST ENDED! You achieved the time limit\n')
            test_end = ctime()
            pass

    # Ending global variables
    t_global_end = time()
    test_duration = t_global_end - t_global_start
    test_hit_duration = 0
    test_miss_duration = 0

    # Input data analise
    for x in range(len(hit_duration)):
        test_hit_duration += hit_duration[x]

    for x in range(len(miss_duration)):
        test_miss_duration += miss_duration[x]

    if number_of_hits != 0:
        accuracy = (number_of_hits / number_of_types) * 100
        type_hit_average_duration = test_hit_duration / number_of_hits
    else:
        accuracy = 0
        type_hit_average_duration = 0

    if test_miss_duration != 0:
        type_miss_average_duration = test_miss_duration / (number_of_types - number_of_hits)
    else:
        type_miss_average_duration = 0

    if iteration != 0:
        type_average_duration = test_duration / iteration
    else:
        type_average_duration = 0

    # Update dictionary
    Total_inputs.update({'accuracy': accuracy, 'inputs': list_input,
                         'number_of_hits': number_of_hits,
                         'number_of_types': number_of_types,
                         'test_duration': test_duration,
                         'test_start': test_start,
                         'test_end': test_end,
                         'type_average_duration': type_average_duration,
                         'type_hit_average_duration': type_hit_average_duration,
                         'type_miss_average_duration': type_miss_average_duration
                         })
    pprint(Total_inputs)

def main():

    # Use argparse for mode selection
    parser = argparse.ArgumentParser(description='PSR - TP1')

    parser.add_argument('-mv', '--max_value', type=int, help='Maximum number of iterations')
    parser.add_argument('-utm', '--use_time_mode', type=int, help='Number of seconds for the test', default=0)
    args = vars(parser.parse_args())
    print(args)

    max_iteration = args['max_value']
    max_time_seconds = args['use_time_mode']

    print('Press any key to start')
    pressed_key = readchar.readchar()


    print("\nStarting Test in 3\n")
    sleep(0.75)
    print("Starting Test in 2\n")
    sleep(0.75)
    print("Starting Test in 1\n")
    sleep(0.75)
    print("GO!!!\n")

    test(' ', max_iteration, max_time_seconds)


if __name__ == "__main__":
    main()
