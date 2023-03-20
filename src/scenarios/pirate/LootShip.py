from ..AbstractScenario import *


class LootShip(Scenario):

    def __init__(self, character, game_running):
        super().__init__(character, game_running)

    def run(self):
        role = self.character.role
        skills = self.character.skills
        print("While stalking the asteroid belt, you come across a hapless asteroid mining vessel.\n"
              "\"Avast me hearties!\" Your captain cries,\"Tis our lucky day\"\n")

        choices = ["Board the ship", "Leave the ship"]

        # Add the option to scan the ship if the player is an engineer
        if role == 'engineer':
            choices.append("Scan ship for secret cargo")

        # Add the option to negotiate if the player is a communications officer
        if role == 'communications officer':
            choices.append("Fire a warning shot, and demand negotiations")

        selection = choice_input(choices)

        # If the player chose to board the ship, success = gold & platinum, failure = Game Over
        if selection == 1:
            print("\nYou board the ship with your rest of your ruthless crew, the mining vessel captain has boarded "
                  "himself and his crew in the bridge.\n \"You're up Rookie!\" yells one of your crew mates... ")
            if chance_modifier(0.1 * float(skills["combat"])):
                print("\nThe poor miners are outmatched by your superior combat skills, and give up. Once securing the "
                      "crew, you make off with their haul of mined gold and platinum.")
                self.character.add_item('gold & platinum')
                self.character.display_inventory()
            else:
                self.end_game(
                    "\nYou put up a valiant fight, but ultimately, your combat skills let you down and you are killed\n"
                    "by the mining vessel crew.")

        # If the player chose to leave the ship alone nothing happens
        elif selection == 2:
            print("\nYou decide to leave the mining vessel alone and continue on your way.")

        # Option 3 is only available if the player is an engineer or a communications officer
        elif selection == 3:
            # If the player chose to scan the ship, success = jet fuel + gold & platinum , failure = nothing
            if role == 'engineer':
                print("\nYou approach the mining vessel and scan it for valuable resources.\n")
                if chance_modifier(0.1 * float(skills["engineering"])):
                    print("You discover a secret cargo of experimental engine fuel! Informing the landing team,\n"
                          "they masterfully cause chaos on board the mining vessel while you steal the jet fuel.\n"
                          "The operation goes off with out a hitch and you return to your ship to find your crew\n"
                          "also managed to steal a bounty of mined gold and platinum. In recognition of your\n"
                          "engineering skills, you get a share of the loot.")
                    self.character.add_item('jet fuel')
                    self.character.display_inventory()
                else:
                    print(
                        "\nYou find no valuable resources on the ship. Perhaps with higher engineering skills you\n"
                        "could have discovered something useful. For not finding anything, you get a stern talking to\n"
                        "from your captain and don't get a share of the loot.")

            # If the player chose to negotiate, success = gold & platinum, failure = Game Over
            elif role == "communications officer":
                print("You approach the mining vessel and hail them on the radio...")
                if chance_modifier(0.1 * float(skills["leadership"])):
                    print("The captain of the mining vessel is impressed by your leadership skills and offers you a "
                          "generous amount of their mined haul to leave them alone.")
                    self.character.add_item('gold & platinum')
                    self.character.display_inventory()
                else:
                    self.end_game("The negotiations go poorly. While you stumbled along, trying to sound intimidating\n"
                                  "and tough, the miners were locking their scopes on to your ships fuel lines,\n"
                                  "and opened fire, destroying your ships ability to move. The miners hail for navy\n"
                                  "assistance and leave you and your crew stranded awaiting arrest. Perhaps with\n"
                                  "higher leadership skills you could have been more convincing.")