from abc import ABC, abstractmethod
from ..mechanics import *


class Scenario(ABC):

    def __init__(self, character, game_running):
        self.character = character
        self.game_running = game_running

    def skill_input(self, input_text):
        if self.character.available_skill_points == 0:
            print('You have no points left to allocate to your skills!\n')
            return

        allocated_points = 0
        while allocated_points == 0:
            point_input = number_input(input_text)
            if point_input > self.character.max_point_allocation or point_input < 1:
                print('Please enter a number between 1 and 10')
            elif point_input > self.character.available_skill_points:
                print('You do not have enough points left')
            else:
                allocated_points = point_input

        self.character.available_skill_points -= allocated_points
        print(f"You have {self.character.available_skill_points} skill points left to allocate\n")
        return allocated_points

    def get_character(self):
        return self.character

    def end_game(self, reason):
        self.game_running = False
        print(reason)

    def is_game_running(self):
        return self.game_running

