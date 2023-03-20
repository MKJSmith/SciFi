from .mechanics import *


class Character:
    max_point_allocation = 10

    def __init__(self):
        self.available_skill_points = 20
        self.name = ''
        self.role = ''
        self.ship = ''
        self.items = []
        self.skills = {
            "piloting": 0,
            "leadership": 0,
            "combat": 0,
            "engineering": 0
        }

    def customize(self):
        print("Before we begin, let's customize your character.\n")
        name = input("What is your character's name? ")
        print(
            f"\nWelcome, {name}! As you prepare to embark on this dangerous mission, you must choose how to allocate "
            "your skills. You only have 20 skill points, assign them wisely...\n")
        self.name = name

        for skill in self.skills:
            if self.available_skill_points > 0:
                self.skills[skill] = self.skill_input(
                    f"Enter a number from 1 to 10 to represent your {skill} skills: ")
        self.display_current_stats()

    def display_current_stats(self):
        print('Your current skill stats:')
        for skill, value in self.skills.items():
            print(skill, ':', value)
        print('\n')

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_inventory(self):
        print('Your current inventory:')
        for item in self.items:
            print('-', item)

    def skill_input(self, input_text):
        if self.available_skill_points == 0:
            print('You have no points left to allocate to your skills!\n')
            return

        allocated_points = 0
        while allocated_points == 0:
            point_input = number_input(input_text)
            if point_input > self.max_point_allocation or point_input < 1:
                print('Please enter a number between 1 and 10')
            elif point_input > self.available_skill_points:
                print('You do not have enough points left')
            else:
                allocated_points = point_input

        self.available_skill_points -= allocated_points
        print(f"You have {self.available_skill_points} skill points left to allocate\n")
        return allocated_points
