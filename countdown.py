#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import operator

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
PLATES_TO_DRAW = {"doubles": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "simples": [25, 50, 75, 100]}
# Operands list
# OPERANDS_LIST = {"add" : "+", "substraction" : "-", "multiplication" : "*", "division" : "/"}
OPERANDS_LIST = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
# Plates drawn
plates_drawn = []
# List of intermediate results
intermediates_results = []
# Final calculated number
final_result = 0
# Number to calculate
# number_to_calculate = 0
# Continue game
continue_game = True


# Selected operand
# selected_operand = ""


# Generate random number to calculate in range 101, 999
def generate_nb_to_calculate():
    """

    :return: number to calculate
    """
    nb_to_calculate = random.randint(NB_TO_CALCULATE_MIN, NB_TO_CALCULATE_MAX)
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
        plate_drawn = random.randint(PLATES_TO_DRAW[random_choice][0],
                                     PLATES_TO_DRAW[random_choice][len(PLATES_TO_DRAW[random_choice]) - 1])
        if random_choice == "simple":
            while plate_drawn in arr_plates:
                plate_drawn = random.randint(PLATES_TO_DRAW[random_choice][0],
                                             PLATES_TO_DRAW[random_choice][len(PLATES_TO_DRAW[random_choice]) - 1])
        else:
            while arr_plates.count(plate_drawn) > 1:
                plate_drawn = random.randint(PLATES_TO_DRAW[random_choice][0],
                                             PLATES_TO_DRAW[random_choice][len(PLATES_TO_DRAW[random_choice]) - 1])
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


def select_list_nb(list_nb_init, list_nb_res):
    """

    :param list_nb_init:
    :param list_nb_res:
    :return:
    """
    selected_list = 0

    # Select list
    while selected_list not in (1, 2):
        try:
            selected_list = int(input(f"Please select a list to choose a number from : \n"
                                      f"1 - Initial numbers :{list_nb_init}\n"
                                      f"2 - Calculated numbers : {list_nb_res}\n"))
        except ValueError:
            print("Error : must choose a number between 1 and 2.")
        if selected_list not in (1, 2):
            print("Error : must choose a number between 1 and 2.")
    if selected_list == 1:
        return list_nb_init
    else:
        return list_nb_res

# Select which list to choose from and a number
def select_number(list_sel):
    """

    :param list_sel:
    :return:
    """

    selected_plate = 0

    # Select plate
    while selected_plate not in list_sel:
        try:
            selected_plate = int(input(f"Please select a number : \n"
                                       f"Available numbers :{list_sel}\n"))
        except ValueError:
            print("Error : must choose a number from the displayed list.")
        if selected_plate not in list_sel:
            print("Error : must choose a number from the displayed list.")

    return selected_plate

# Select operand
def select_operand():
    """

    :return:
    """
    operand = ""
    try:
        operand = str(input(f"Choose operand : {OPERANDS_LIST}"))
    except ValueError:
        print("Error : must choose operator from displayed list.")
    if operand not in OPERANDS_LIST:
        print("Error : must choose operator from displayed list.")
    return operand

# Compare results
def compare_results(player_result, init_result):
    """

    :param player_result:
    :param init_result:
    :return:
    """
    if player_result == init_result:
        score = "Le compte est bon !\n Patrice Laffont would be proud of you !"
    else:
        score = "Presque !"
    return score

# Calculate intermediate result
def calc_inter_result(number1, number2, operand):
    """

    :param number1:
    :param number2:
    :param operand:
    :return:
    """
    calculated_result = OPERANDS_LIST[operand](number1, number2)
    return calculated_result

# Display operation
def display_operation(selected_oper, selected_number1, selected_number2, calc_result):
    """

    :param calc_result:
    :param selected_oper:
    :param selected_number1:
    :param selected_number2:
    :return:
    """
    print(f"{selected_number1} {selected_oper} {selected_number2} = {calc_result}")



print("Welcome to \"Le compte est bon !\"")

# Draw plates
plates_drawn = draw_plates(plates_drawn)

# Display plates
print(f"Here are the plates drawn : \n {plates_drawn}")

# Display number to calculate
number_to_calculate = generate_nb_to_calculate()
print(f"Here is the number to calculate : {number_to_calculate}")

# First turn (no intermediate results)
intermediate_result1 = select_number(plates_drawn)
plates_drawn = delete_number(intermediate_result1,plates_drawn)
intermediate_result2 = select_number(plates_drawn)
selected_operand = select_operand()
intermediates_results.append(calc_inter_result(intermediate_result1, intermediate_result2, selected_operand))
plates_drawn = delete_number(intermediate_result2,plates_drawn)
# test = len(intermediates_results) - 1
display_operation(selected_operand, intermediate_result2, intermediate_result2,
                  intermediates_results[len(intermediates_results) - 1])

while continue_game:
    # Select numbers
    list_plate = select_list_nb(plates_drawn, intermediates_results)
    intermediate_result1 = select_number(list_plate)
    if list_plate == plates_drawn:
        plates_drawn = delete_number(intermediate_result1,plates_drawn)
    else:
        intermediates_results = delete_number(intermediate_result1, intermediates_results)
    list_plate = select_list_nb(plates_drawn, intermediates_results)
    intermediate_result2 = select_number(list_plate)
    if list_plate == plates_drawn:
        plates_drawn = delete_number(intermediate_result2,plates_drawn)
    else:
        intermediates_results = delete_number(intermediate_result2, intermediates_results)
    # Select operator
    selected_operand = select_operand()
    # Calculate intermediate result and add it to list
    intermediates_results.append(calc_inter_result(intermediate_result1, intermediate_result2, selected_operand))
    # Display operation
    display_operation(selected_operand, intermediate_result1, intermediate_result2,
                      intermediates_results[len(intermediates_results) - 1])

    # Continue game or not
    continue_game = int(input(f"Continue game ?\n 1 - Yes\n 2 - No"))
    if continue_game == 1:
        continue_game = True
    else:
        continue_game = False

# Display final result
print(compare_results(intermediates_results[len(intermediates_results) - 1], number_to_calculate))
