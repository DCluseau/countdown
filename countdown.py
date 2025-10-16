#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Le programme permet à l’utilisateur de jouer à ce jeu célèbre. Il tire au sort un nombre à obtenir entre 101 et 999, ainsi que 6 plaques – portant un nombre – tirés parmi 24 réparties ainsi : chaque nombre de 1 à 10 est présent 2 fois, et les nombres 25, 50, 75 et 100 sont présents en un seul exemplaire.
# A chaque tour de jeu, l’utilisateur sélectionne une opération (addition, soustraction, multiplication, division) et 2 nombres parmi les plaques restantes et les nombres (restants) obtenus lors des opérations précédentes. L’opération appliquée à ces nombres (qui ne sont alors plus utilisables) fournit alors un nouveau nombre.
# L’utilisateur peut, quand il estime ne pas pouvoir se rapprocher davantage du nombre à obtenir, indiquer qu’il souhaite arrêter le jeu (en indiquant si besoin quel nombre parmi ceux obtenus et restants est le nombre qu’il a obtenu), celui-ci s’arrêtant également lorsqu’il ne reste plus de plaque disponible et un seul nombre résultant d’opérations.
# Le programme indique alors à l’utilisateur si « le compte est bon » (le nombre à obtenir a été atteint) ou s’il n’a obtenu qu’un nombre approchant le nombre à obtenir.

# Constants
# Number to calculate
NB_TO_CALCULATE_MIN = 101
NB_TO_CALCULATE_MAX = 999
# Number of plates to draw
NB_DRAWN_PLATES = 6
# Plates
PLATES_TO_DRAW = {"doubles" : [1,2,3,4,5,6,7,8,9,10], "simples" : [25, 50, 75, 100]}
# Operands list
# OPERANDS_LIST = {"add" : "+", "substraction" : "-", "multiplication" : "*", "division" : "/"}
OPERANDS_LIST = ("+", "-", "*", "/")
# Plates drawn
plates_drawn = []
# List of intermediate results
intermediates_results = []
# Final calculated number
final_result = 0
# Number to calculate
number_to_calculate = 0

# Generate random number to calculate in range 101, 999
def generate_nb_to_calculate():
    """

    :return: number to calculate
    """
    nb_to_calculate = random.randint(NB_TO_CALCULATE_MIN,NB_TO_CALCULATE_MAX)
    return nb_to_calculate

# Draw 6 plates
def draw_plates(arr_plates):
    """

    :param arr_plates: list of drawn plates
    :return: list of drawn plates
    """
    # For each plate, generate random choice between simple or double
    for i in range(NB_DRAWN_PLATES):
        random_choice = random.choice(list(PLATES_TO_DRAW.keys()))
        plate_drawn = random.randint(PLATES_TO_DRAW[random_choice][0],PLATES_TO_DRAW[random_choice][len(PLATES_TO_DRAW[random_choice]) - 1])
        if random_choice == "simple":
            while plate_drawn in arr_plates:
                plate_drawn = random.randint(PLATES_TO_DRAW[random_choice][0],PLATES_TO_DRAW[random_choice][len(PLATES_TO_DRAW[random_choice]) - 1])
        else:
            while arr_plates.count(plate_drawn) > 1:
                plate_drawn = random.randint(PLATES_TO_DRAW[random_choice][0],PLATES_TO_DRAW[random_choice][len(PLATES_TO_DRAW[random_choice]) - 1])
        arr_plates.append(plate_drawn)
    return arr_plates

# Display plates
def display_plates(arr_plates):
    """

    :param arr_plates:
    :return:
    """
    print(arr_plates)

# Add intermediate result to list
def add_intermediate_result(inter_result, arr_results):
    """

    :param inter_result:
    :param arr_results:
    :return: arr_results
    """
    arr_results.append(inter_result)
    return arr_results

# Delete number used (from list of plates or list of intermediate results)
def delete_number(number_to_delete, list_numbers):
    """

    :param number_to_delete:
    :param list_numbers:
    :return:
    """
    if number_to_delete in list_numbers:
        list_numbers.remove(number_to_delete)
    return list_numbers