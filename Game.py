from src import *


class Game:

    def __init__(self):
        self.game_running = False
        self.character = Character()

    def pirate_scenarios(self):
        LootShip(self.character, self.game_running).run()

    def navy_scenarios(self):
        pass

    def miner_scenarios(self):
        pass

    def common_scenarios(self):
        pass

    def end_game(self,message_string):
        self.game_running = False
        print(message_string, '\n')
        print('GAME OVER')

    def play(self):
        self.game_running = True
        introduction()
        self.character.customize()
        JoinSpaceship(self.character, self.game_running).run()
        ship = self.character.ship
        while self.game_running:
            if ship == 'navy':
                self.navy_scenarios()
            elif ship == 'pirate':
                self.pirate_scenarios()
            elif ship == 'mining':
                self.miner_scenarios()
            # regardless of ship type, play the common scenarios last
            self.common_scenarios()


# end Game _____________________________________________________________________________________________________________


def introduction():
    print(
        "Welcome to Wormhole - a SciFi adventure src! You are a space traveler in search of a way to get to a new "
        "galaxy.\nYou have just joined the crew of a spaceship that is about to travel through a dangerous "
        "wormhole.\nYour mission is to help the crew make it to the other side safely. Good luck!\n")
