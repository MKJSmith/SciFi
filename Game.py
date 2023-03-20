from src import *


class Game:

    def __init__(self):
        self.game_running = True
        self.character = Character()

    def run_scenario(self, scenario):
        scenario.run()
        self.game_running = scenario.is_game_running()

    def pirate_scenarios(self):
        self.run_scenario(LootShip(self.character, self.game_running))

    def navy_scenarios(self):
        pass

    def miner_scenarios(self):
        pass

    def common_scenarios(self):
        self.run_scenario(Wormhole(self.character, self.game_running))

    def end_game(self, message_string):
        self.game_running = False
        print(message_string, '\n')
        print('GAME OVER')

    def replay_prompt(self):
        print('\n----GAME OVER-------------------------------------------------------------------\n')
        selection = choice_input(['Play again', 'Quit'])
        if selection == 1:
            self.__init__()
            self.play()
        else:
            print('Thanks for playing!')
            exit(1)

    def play(self):
        introduction()
        self.character.customize()
        self.run_scenario(JoinSpaceship(self.character, self.game_running))
        ship = self.character.ship
        while self.game_running:
            if ship == 'navy':
                self.navy_scenarios()
            elif ship == 'pirate':
                self.pirate_scenarios()
            elif ship == 'mining':
                self.miner_scenarios()
            # regardless of ship type, play the common scenarios last
            if self.game_running:
                self.common_scenarios()

        self.replay_prompt()


# end Game _____________________________________________________________________________________________________________


def introduction():
    print(
        "Welcome to Wormhole - a SciFi adventure text based adventure game! You are a space traveler in search of a "
        "way to get to a new galaxy.\nYou have just joined the crew of a spaceship that is about to travel through a "
        "dangerous wormhole.\nYour mission is to help the crew make it to the other side safely. Good luck!\n")
