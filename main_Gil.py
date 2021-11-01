#!/usr/bin/env python3
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
    # Ask for all the entries and put them in a list

    miss_duration = []  # Analtino
    hit_duration = []  # Analtino
    Total_inputs = {}  # Analtino
    number_of_hits = 0  # Analtino
    number_of_types = 0  # Analtino
    pressed_keys = []  # empty list to start with
    list_input = []
    iteration = 0
    dur = 0;

    t_global_start = time()
    #verificar o modo tempo o quantidade
    if max_time_seconds == 0:
        while True:
            letter = random.choice(string.ascii_lowercase)  # Gera uma letra aleatoria
            # Apresentar a primeira letra que o utilizador deve inserir
            print('Type ' + Fore.LIGHTBLUE_EX + str(letter) + Style.RESET_ALL + ' or space to stop: ')
            test_start = ctime()  # Guarda a data de inicio
            t_local_start = time()  # inicia um temporizador
            pressed_key = readchar.readchar()  # Guarda o caracter inserido pelo utilizador
            iteration += 1

            if pressed_key == stop_key:  # Se o caracter inserido for igual a chave para parar
                print('\nTEST ENDED! You pressed space.\n')
                break  # Sai do ciclo
            else:
                pressed_keys.append(pressed_key)  # Guardar o caracter inserido num Dicionario
                t_local_end = time()  # Fim do temporizador
                test_end = ctime()  # Guarda a data de fim

                if pressed_key == letter:  # Se o caracter inserido for igual a chave para parar
                    print('You pressed ' + Fore.GREEN + str(pressed_key) + Style.RESET_ALL + ' so your answer is CORRECT!')
                    number_of_hits += 1  # numero de letras acertadas
                    number_of_types += 1  # numero de letras inseridas
                    hit_duration.append(t_local_end - t_local_start)  # Guarda o tempo que o utilizador levou para acertar
                else:
                    print('You pressed ' + Fore.RED + str(pressed_key) + Style.RESET_ALL + ' so your answer is INCORRECT!')
                    number_of_types += 1  # numero de letras inseridas
                    miss_duration.append(t_local_end - t_local_start)  # Guarda o tempo que o utilizador levou mas falhou

            t_local_end = time()  # Fim do temporizador
            input_duration = t_local_end - t_local_start  # Guarda o tempo que o utilizador levou mas falho

            # Com base no nameTupple criado inicialmente de nome "Input" criar um elemento da classe e adicionar a lista
            Tuple = Input(str(letter), str(pressed_key), str(input_duration))
            list_input.append(Tuple)  # Adicionar a Lista "list_input"


            if iteration == max_iteration:  # Se o numero de caracteres inseridos for igual ao
                # valor maximo predifinido
                print('\nTEST ENDED! You achieved the maximum iteration\n')
                break  # Sai do ciclo
    else:
        try:
            with timeout(max_time_seconds, exception=RuntimeError):
                while True:
                    letter = random.choice(string.ascii_lowercase)  # Gera uma letra aleatoria
                    # Apresentar a primeira letra que o utilizador deve inserir
                    print('Type ' + Fore.LIGHTBLUE_EX + str(letter) + Style.RESET_ALL + ' or space to stop: ')
                    test_start = ctime()  # Guarda a data de inicio
                    t_local_start = time()  # inicia um temporizador
                    pressed_key = readchar.readchar()  # Guarda o caracter inserido pelo utilizador
                    iteration += 1

                    if pressed_key == stop_key:  # Se o caracter inserido for igual a chave para parar
                        print('\nTEST ENDED! You pressed space.\n')
                        break  # Sai do ciclo
                    else:
                        pressed_keys.append(pressed_key)  # Guardar o caracter inserido num Dicionario
                        t_local_end = time()  # Fim do temporizador
                        test_end = ctime()  # Guarda a data de fim

                        if pressed_key == letter:  # Se o caracter inserido for igual a chave para parar
                            print('You pressed ' + Fore.GREEN + str(pressed_key) + Style.RESET_ALL + ' so your answer is CORRECT!')
                            number_of_hits += 1  # numero de letras acertadas
                            number_of_types += 1  # numero de letras inseridas
                            hit_duration.append(t_local_end - t_local_start)  # Guarda o tempo que o utilizador levou para acertar
                        else:
                            print('You pressed ' + Fore.RED + str(pressed_key) + Style.RESET_ALL + ' so your answer is INCORRECT!')
                            number_of_types += 1  # numero de letras inseridas
                            miss_duration.append(t_local_end - t_local_start)  # Guarda o tempo que o utilizador levou mas falhou

                    t_local_end = time()  # Fim do temporizador
                    input_duration = t_local_end - t_local_start  # Guarda o tempo que o utilizador levou mas falho

                    # Com base no nameTupple criado inicialmente de nome "Input" criar um elemento da classe e adicionar a lista
                    Tuple = Input(str(letter), str(pressed_key), str(input_duration))
                    list_input.append(Tuple)  # Adicionar a Lista "list_input"
        except RuntimeError:
            print('\nTEST ENDED! You achieved the time limit\n')
            pass

    t_global_end = time()
    test_duration = t_global_end - t_global_start
    test_hit_duration = 0
    test_miss_duration = 0

    for x in range(len(hit_duration)):  # usar o tamanho da lista como valor maximo do ciclo
        test_hit_duration += hit_duration[x]

    for x in range(len(miss_duration)):  # usar o tamanho da lista como valor maximo do ciclo
        test_miss_duration += miss_duration[x]

    if number_of_hits != 0:
        accuracy = (number_of_hits / number_of_types) * 100  # Percentagem de acertos
        type_hit_average_duration = test_hit_duration / number_of_hits
    else:
        accuracy = 0
        type_hit_average_duration = 0

    if test_miss_duration != 0:
        type_miss_average_duration = test_miss_duration / (number_of_types - number_of_hits)
    else:
        type_miss_average_duration = 0

    try:
        type_average_duration = test_duration / iteration
    except:
        pass

    try:
        Total_inputs.update({'accuracy': accuracy, 'inputs': list_input,
                         'number_of_hits': number_of_hits,
                         'number_of_types': number_of_types,
                         'test_duration': test_duration,
                         'test_end': test_end,
                         'test_start': test_start,
                         'type_average_duration': type_average_duration,
                         'type_hit_average_duration': type_hit_average_duration,
                         'type_miss_average_duration': type_miss_average_duration
                         })
        pprint(Total_inputs)
    except:
        print ('\nAn error as ocurred while trying to show your stats...\n')


def main():
    parser = argparse.ArgumentParser(description='PSR - TP1')

    parser.add_argument('-mv', '--max_value', type=int, help='Maximum number of iterations')
    parser.add_argument('-utm', '--use_time_mode', type=int, help='Number of seconds for the test', default=0)
    args = vars(parser.parse_args())
    print(args)

    max_iteration = args['max_value']
    max_time_seconds = args['use_time_mode']

    print('Press any key to start')
    pressed_key = readchar.readchar()  # Guarda o caracter inserido pelo utilizador

    print("Starting Test")
    sleep(1)

    test(' ', max_iteration, max_time_seconds)


if __name__ == "__main__":
    main()
