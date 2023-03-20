from ..AbstractScenario import *


class JoinSpaceship(Scenario):

    def __init__(self, character, game_running):
        super().__init__(character, game_running)

    def run(self):
        print("As you wander through the spaceport, you see three different spacecraft that are about to depart.\n"
              "Which one do you want to join?\n")

        selection = choice_input([
            "Pirate ship (+3 combat, -2 leadership, +1 engineering)",
            "Royal navy ship (+3 leadership, +1 combat)",
            "Asteroid mining vessel (+3 engineering, -2 combat, +1 piloting)"
        ])

        modified_skills = {}
        selected_ship = None

        if selection == 1:
            print("You have joined a pirate ship crew!")
            modified_skills = {
                "leadership": -2,
                "combat": 3,
                "engineering": 1
            }
            selected_ship = 'pirate'
        elif selection == 2:
            print("You have joined a royal navy crew!")
            modified_skills = {
                "leadership": 3,
                "combat": 1,
            }
            selected_ship = 'navy'
        elif selection == 3:
            print("You have joined an asteroid mining vessel!")
            modified_skills = {
                "combat": -2,
                "engineering": 3
            }
            selected_ship = 'mining'

        # Update the characters skills based off the selection
        for skill, value in modified_skills.items():
            try:
                self.character.skills[skill] += value
            except KeyError:
                pass
        self.character.ship = selected_ship
        # Display our stats now we're done
        self.character.display_current_stats()
