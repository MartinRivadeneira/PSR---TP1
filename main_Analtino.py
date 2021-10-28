#!/usr/bin/env python3
import json
from pprint import pprint

from colorama import Fore, Back, Style
import readchar
import argparse
import random
import string
from time import time
from collections import namedtuple
from time import time, ctime
Input = namedtuple('Input', ['requested', 'received', 'duration'])

def printAllCharsUpTo(stop_char):

    print('I dont know how to do it yet')

    print('Printing all the values up to stop_char ' + str(stop_char))
    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))

def test(stop_key, max_iteration):

    # Ask for all the entries and put them in a list
    requested = []
    received = []
    duration = []
    miss_duration=[]
    hit_duration = []
    inputs_1 = []
    Total_inputs = {}
    bob=[]
    number_of_hits = 0
    number_of_types = 0
    pressed_keys = [] # empty list to start with
    list_input = []
    iteration = 0

    t_global_start = time()

    while True:
        test_start = ctime() # Analtino
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
                t_local_end = time()
                print('You pressed ' + Fore.GREEN + str(pressed_key) + Style.RESET_ALL + ' so your answer is CORRECT!')
                test_end = ctime()       #Analtino
                number_of_hits += 1      #Analtino
                number_of_types += 1     #Analtino
                received.append(pressed_key) #Analtino
                duration.append(t_local_end - t_local_start) #Analtino
                hit_duration.append(t_local_end - t_local_start)#Analtino
            else:
                t_local_end = time()
                print('You pressed ' + Fore.RED + str(pressed_key) + Style.RESET_ALL + ' so your answer is INCORRECT!')
                test_end = ctime()          #Analtino
                number_of_types += 1        #Analtino
                received.append(pressed_key)#Analtino
                duration.append(t_local_end - t_local_start)  # Analtino
                miss_duration.append(t_local_end - t_local_start )#Analtino

        if iteration == max_iteration:
            print('\nTEST ENDED! You achieved the maximum iteration\n')
            break



        input_duration = t_local_end - t_local_start

        Tuple = Input(requested = letter, received = pressed_key, duration = input_duration)
        list_input.append(Tuple)

    t_global_end = time()
    test_total_duration = t_global_end - t_global_start

    test_total_duration = 0
    test_hit_duration = 0
    test_miss_duration = 0

    for x in range(len(duration)):
        test_total_duration += duration[x]

    for x in range(len(hit_duration)):
        test_hit_duration += hit_duration[x]

    for x in range(len(miss_duration)):
        test_miss_duration += miss_duration[x]

    accuracy = (number_of_hits / number_of_types) * 100

    type_average_duration = test_total_duration / max_iteration
    type_hit_average_duration = test_hit_duration / number_of_hits
    type_miss_average_duration = test_miss_duration / (number_of_types - number_of_hits)

    Total_inputs.update({'accuracy': accuracy, 'inputs': str(inputs_1),
    'number_of_hits': number_of_hits,
    'number_of_types': number_of_types,
     'test_duration': test_total_duration,
    'test_end': test_end,
    'test_start': test_start,
    'type_average_duration': type_average_duration,
    'type_hit_average_duration': type_hit_average_duration,
    'type_miss_average_duration': type_miss_average_duration
    })

    print('The keys you pressed are: ' + str(pressed_keys))

    print('\nList of inputs is:\n')
    for i in list_input:
        print(str(i))

    print('\nTest duration: ' + str(test_total_duration) + 's')
    pprint(json.dumps(Total_inputs, sort_keys=True, indent=2))
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