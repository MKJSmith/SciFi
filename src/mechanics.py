import random


def chance_modifier(chance_of_success_float):
    """
    Returns True or False based on a chance of success given
    :type chance_of_success_float: float
    :param chance_of_success_float: between 0 and 1
    :return: True or False
    """
    return random.random() <= chance_of_success_float


def number_input(input_text):
    number = None
    while number is None:
        try:
            number = int(input(input_text))
        except ValueError:
            print('please enter a number\n')
    return number


def choice_input(choices):
    """
    :type choices: list
    :param choices:
    :return:
    """
    number_of_choices = choices.__len__()
    choices_string = 'What would you like to do?\n'
    for i in range(number_of_choices):
        choices_string += f'{i + 1}. {choices[i]}\n'

    selection = None
    while selection is None:
        selection = number_input(choices_string)
        if selection < 1 or selection > number_of_choices:
            selection = None
            print(f'please enter a number from 1 - {number_of_choices}\n')
    return selection
