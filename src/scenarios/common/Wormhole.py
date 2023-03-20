from ..AbstractScenario import *


class Wormhole(Scenario):

    def __init__(self, character, game_running):
        super().__init__(character, game_running)

    def run(self):
        skills = self.character.skills
        print("\nYour crew has detected a strange anomaly beyond Neptune, a wormhole!\nWhere could it lead?\n"
              "Why is it here?\nAnswers can only be found if you approach it and decide how your ship will react...")

        action = choice_input(["Proceed with caution", "Blast through the wormhole", "Turn back"])

        if action == 1:
            # Maybe here you have a 50/50 chance of making it through?
            self.end_game("You made it through the wormhole safely!")
        elif action == 2:
            if skills['piloting'] < 5:
                # There is 1 in 1000 chance of actually making it regardless of piloting skill
                if chance_modifier(0.1):
                    self.end_game(
                        "Some how, by an unbelievable stroke of luck, your reckless piloting has resulted in you and "
                        "your crew making it through the wormhole in one piece, albeit at the expense of your ships "
                        "engines, and life support system...\nLets hope there's a good Samaritan near by to answer "
                        "your distress call. 😬")
                self.end_game("Your ship was destroyed in the wormhole.")
            else:
                self.end_game("\"Punch it Chewy!\" You cry out, causing much confusion to your crew mates.\n"
                              "Using your impressive piloting skills, you've manage to avoid disaster, and make it "
                              "through to\n the other side! \nCongratulations you've beaten Wormhole\n")
        elif action == 3:
            self.end_game(
                "You try to turn the ship back, but the wormhole's gravity has warped your instruments, and the crew\n"
                "has started to panic. In all the commotion your ship enters the wormhole at the incorrect angle,\n"
                "riping it to pieces in a spectacular explosion. This disaster is broadcast as a warning across the\n"
                "solar system about the dangers of wormholes.")
