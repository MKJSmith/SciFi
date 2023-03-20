# Single File version of the Game
import random

# Globals:
debug = True
game_running = True
available_skill_points = 20
max_point_allocation = 10
character = {
    "name": '',
    "role": '',
    "ship": '',
    "items": [],
    "skills": {
        "piloting": 0,
        "leadership": 0,
        "combat": 0,
        "engineering": 0
    }
}


# HELPERS ----------------------------------------------------------------------

def skill_input(input_text):
    global available_skill_points
    global max_point_allocation
    if available_skill_points == 0:
        print('You have no points left to allocate to your skills!\n')
        return

    allocated_points = 0
    while allocated_points == 0:
        point_input = number_input(input_text)
        if point_input > max_point_allocation or point_input < 1:
            print('Please enter a number between 1 and 10')
        elif point_input > available_skill_points:
            print('You do not have enough points left')
        else:
            allocated_points = point_input

    available_skill_points -= allocated_points
    print(f"You have {available_skill_points} skill points left to allocate\n")
    return allocated_points


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


def display_current_stats():
    global character
    print('Your current skill stats:')
    for skill, value in character['skills'].items():
        print(skill, ':', value)
    print('\n')


def display_inventory():
    print('\nYour current inventory:')
    for item in character['items']:
        print('-', item)


# Enter a percentage chance of success as a float between 0.0 and 100.0
def chance_modifier(chance_of_success_float):
    """
    Returns True or False based on a chance of success given
    :type chance_of_success_float: float
    :param chance_of_success_float: between 0 and 1
    :return: True or False
    """
    global debug
    score = round(random.random(), 4)
    result = score <= chance_of_success_float
    if debug:
        print(f'Chance of success: {chance_of_success_float * 100}% - Result: {score * 100}%')
    return result


# Helper to end the game if a choice is catastrophic
def end_game(message_string):
    global game_running
    game_running = False
    print(message_string, '\n')
    print('GAME OVER')


# ------------------------------------------------------------------------------


# CHARACTER SETUP --------------------------------------------------------------
def customize_character():
    global character
    global available_skill_points
    print("Before we begin, let's customize your character.\n")
    name = input("What is your character's name? ")
    print(f"\nWelcome, {name}! As you prepare to embark on this dangerous mission, you must choose how to allocate your"
          f"skills. You only have 20 skill points, assign them wisely...\n")
    character['name'] = name

    for skill in character['skills']:
        if available_skill_points > 0:
            character['skills'][skill] = skill_input(f"Enter a number from 1 to 10 to represent your {skill} skills: ")
    display_current_stats()


def join_spaceship():
    global character
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
            character['skills'][skill] += value
        except KeyError:
            pass
    character['ship'] = selected_ship
    # Display our stats now we're done
    display_current_stats()


def spaceship_crew_selection():
    global character
    print(f"Welcome aboard, {character['name']}! The captain is looking for a new crew member to help with the mission."
          "\nWhich position would you like to apply for?")

    selection = None
    while selection is None:
        selection = choice_input([
            "Pilot",
            "Engineer",
            "Medical Officer",
            "Communications Officer",
            "Security Officer"
        ])
        selection = validate_selection(selection)

    character['role'] = selection


def validate_selection(selection):
    global character
    skills = character['skills']
    if selection == 1:
        if skills["piloting"] >= 5:
            print("Congratulations! You have been selected as the new pilot.\n")
            return 'pilot'
        else:
            print("Sorry, your piloting skills are not strong enough to be the pilot.\n"
                  "Please choose a different role.")
    elif selection == 2:
        if skills["engineering"] >= 5:
            print("Congratulations! You have been selected as the new engineer")
            return 'engineer'
        else:
            print("Sorry, your engineering skills are not strong enough to be the engineer.\n"
                  "Please choose a different role.\n")
    elif selection == 3:
        print("Congratulations! You have been selected as the new medical officer!\n")
        return 'medic'
    elif selection == 4:
        print("Congratulations! You have been selected as the new communications officer.\n")
        return 'communications officer'
    elif selection == 5:
        if skills["combat"] >= 5:
            print("Congratulations! You have been selected as the new security officer of the spaceship.")
            return 'security'
        else:
            print("Sorry, your combat skills are not strong enough to be the security officer of this crew.\n"
                  "Please choose a different role.")
            return None


# ------------------------------------------------------------------------------

# SCENARIOS --------------------------------------------------------------------
def introduction():
    print("Welcome to Wormhole - a SciFi adventure game! You are a space traveler in search of a way to get to a new "
          "galaxy.\nYou have just joined the crew of a spaceship that is about to travel through a dangerous "
          "wormhole.\nYour mission is to help the crew make it to the other side safely. Good luck!\n")


# Based off the selected ship, pick which scenarios to play
def play_selected_ship_scenarios():
    global character
    global game_running
    ship = character['ship']
    while game_running:
        if ship == 'navy':
            navy_ship_scenarios()
        elif ship == 'pirate':
            pirate_ship_scenarios()
        elif ship == 'mining':
            mining_ship_scenarios()
        # Previous scenarios may have ended the game, so check if it's still running
        if game_running:
            global_scenarios()


# scenarios which all ship types will play
def global_scenarios():
    # TODO: add some more scenarios!
    wormhole_encounter()  # Wormhole encounter is the last scenario to play


# Add any navy specific scenarios here
def navy_ship_scenarios():
    protect_ship()
    # TODO: add some more scenarios!


# Add any pirate specific scenarios here
def pirate_ship_scenarios():
    loot_ship()
    # TODO: add some more scenarios!


# Add any mining specific scenarios here
def mining_ship_scenarios():
    defend_ship()
    # TODO: add some more scenarios!
    # Maybe add a scenario about discovering a derelict ship, with the potential for some horror elements @Ella?


def defend_ship():
    global character
    print("While mining the glorious bounty discovered on the asteroid Psyche, an unknown vessel appears on your "
          "scopes.\nThey won't respond to hails, and it seems they're readying their weapons...\n")
    # TODO: add some options!


def ship_hit_by_asteroid():
    global character


def loot_ship():
    global character
    role = character['role']
    skills = character['skills']
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
            character['items'] += ['gold & platinum']
            display_inventory()
        else:
            end_game(
                "\nYou put up a valiant fight, but ultimately, your combat skills let you down and you are killed by "
                "the mining vessel crew.")

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
                      "they masterfully cause chaos on board the mining vessel while you steal the jet fuel. The\n"
                      "operation goes off with out a hitch and you return to your ship to find your crew also managed\n"
                      "to steal a bounty of mined gold and platinum. In recognition of your engineering skills, you \n"
                      "get a share of the loot.")
                character['items'].append('jet fuel')
                display_inventory()
            else:
                print(
                    "\nYou find no valuable resources on the ship. Perhaps with higher engineering skills you could\n"
                    "have discovered something useful. For not finding anything, you get a stern talking to from your\n"
                    "captain and don't get a share of the loot.")

        # If the player chose to negotiate, success = gold & platinum, failure = Game Over
        elif role == "communications officer":
            print("You approach the mining vessel and hail them on the radio...")
            if chance_modifier(0.1 * float(skills["leadership"])):
                print("The captain of the mining vessel is impressed by your leadership skills and offers you a "
                      "generous amount of their mined haul to leave them alone.")
                character['items'].append('gold & platinum')
                display_inventory()
            else:
                end_game("The negotiations go poorly. While you stumbled along, trying to sound intimidating and\n"
                         "tough, the miners were locking their scopes on to your ships fuel lines, and opened fire,\n"
                         "destroying your ships ability to move. The miners hail for navy assistance and leave you\n"
                         "and your crew stranded awaiting arrest. Perhaps with higher leadership skills you could\n"
                         "have been more convincing.")


def protect_ship():
    global character
    print("While patrolling Saturn's moon Enceladus, you happen to intercept a known pirate vessel harassing some "
          "poor ice miners...\n")
    # TODO: add some options!


# Wormhole is the end game scenario, all roads lead to this!
def wormhole_encounter():
    global character
    skills = character['skills']
    print("\nYour crew has detected a strange anomaly beyond Neptune, a wormhole!\nWhere could it lead?\n"
          "Why is it here?\nAnswers can only be found if you approach it and decide how your ship will react...")

    action = choice_input(["Proceed with caution", "Blast through the wormhole", "Turn back"])

    if action == 1:
        # Maybe here you have a 50/50 chance of making it through?
        end_game("You made it through the wormhole safely!")
    elif action == 2:
        if skills['piloting'] < 5:
            # There is 1 in 1000 chance of actually making it regardless of piloting skill
            if chance_modifier(0.1):
                end_game("Some how, by an unbelievable stroke of luck, your reckless piloting has resulted in you and "
                         "your crew making it through the wormhole in one piece, albeit at the expense of your ships "
                         "engines, and life support system...\nLets hope there's a good Samaritan near by to answer "
                         "your distress call. 😬")
            end_game("Your ship was destroyed in the wormhole.")
        else:
            end_game("\"Punch it Chewy!\" You cry out, causing much confusion to your crew mates.\n"
                     "Using your impressive piloting skills, you've manage to avoid disaster, and make it through to\n"
                     "the other side! \nCongratulations you've beaten Wormhole\n")
    elif action == 3:
        end_game("You try to turn the ship back, but the wormhole's gravity has warped your instruments, and the crew\n"
                 "has started to panic. In all the commotion your ship enters the wormhole at the incorrect angle,\n"
                 "riping it to pieces in a spectacular explosion. This disaster is broadcast as a warning across the\n"
                 "solar system about the dangers of wormholes.")


# ------------------------------------------------------------------------------


# CORE GAME --------------------------------------------------------------------
def main():
    introduction()
    customize_character()
    join_spaceship()
    spaceship_crew_selection()
    play_selected_ship_scenarios()


if __name__ == '__main__':
    # Run the game
    main()
    exit(1)
