from ..AbstractScenario import *


class LootShip(Scenario):

    def __init__(self, character, game_running):
        super().__init__(character, game_running)

    def run(self):
        print("While stalking the asteroid belt, you come across a hapless asteroid mining vessel.\n"
              "\"Avast me hearties!\" Your captain cries,\"Tis our lucky day\"\n")

        selection = choice_input("What do you do?\n"
                                 "1. Board the ship\n"
                                 "2. Negotiate with the captain\n"
                                 "3. Scan the ship for valuable resources\n"
                                 "4. Leave the ship\n", 4)

        if selection == 1:
            print("You board the ship with your rest of your ruthless crew, the mining vessel captain has boarded "
                  "himself and his crew in the bridge.\n \"You're up Rookie!\" yells one of your crew mates... ")
            if chance_modifier(0.1 * float(self.character.skills["combat"])):
                print("You kill the captain and his crew and take the ship for yourself")
            else:
                print("You are killed by the captain and his crew")
                self.game_running = False

        elif selection == 2:
            print("You approach the mining vessel and hail them on the radio.\n")
            if chance_modifier(0.1 * float(self.character.skills["leadership"])):
                print("The captain of the mining vessel is impressed by your leadership skills and offers you a "
                      "generous amount of money to leave him alone.")
            else:
                print("The captain of the mining vessel is not impressed by your leadership skills and shoots you "
                      "dead.")
                self.game_running = False

        elif selection == 3:
            print("You approach the mining vessel and scan it for valuable resources.\n")
            if chance_modifier(0.1 * float(self.character.skills["engineering"])):
                print("You find a large amount of valuable resources on the ship and take them for yourself.")
            else:
                print("You find no valuable resources on the ship.")
                self.game_running = False

        elif selection == 4:
            print("You decide to leave the mining vessel alone and continue on your way.")

        return
