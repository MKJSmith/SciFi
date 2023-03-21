from ..AbstractScenario import *


class EscapeNavy(Scenario):

    def __init__(self, character, game_running):
        super().__init__(character, game_running)

    def run(self):
        skills = self.character.skills
        inventory = self.character.items
        print("You are being chased by the Navy! They are closing in fast! You need to escape!")

        choices = ["Try to outrun them", "Try to Bribe them", "Try to fight them"]

        selection = choice_input(choices)

        if selection == 1:
            if chance_modifier(0.1 * float(skills["piloting"])):
                print("You use your piloting skills to escape the Navy!")
                return
            elif "jet fuel" in inventory:
                print("You use your jet fuel to escape the Navy!")
                return
            else:
                self.end_game("You failed to escape the Navy!")
        if selection == 2:
            if "gold & platinum" in inventory:
                print("You use your gold & platinum to bribe the Navy!")
            else:
                self.end_game("You failed to bribe the Navy!")

        if selection == 3:
            if chance_modifier(0.1 * float(skills["combat"])):
                print("You use your combat skills to defeat the Navy!")
            elif "jet fuel" in inventory:
                print("You use your jet fuel to defeat the Navy!")
            else:
                self.end_game("You failed to defeat the Navy!")


