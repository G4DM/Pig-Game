# Import section

from random import randint

# Random selection to which player is going to start and store actual player

def random_player():
    player_start = randint(1, 3)

    if player_start == 1:
        return 1
    if player_start == 2:
        return 2
    if player_start == 3:
        return 3

current_player = random_player()

# Player turn

def player_turn(current):
    print(f'Now is the turn of player {current}!\n')


# Roll the dice function

def roll_the_dice():
    print("Rolling the dice...")
    print(f'The number rolled is {randint(1, 6)}!')

roll_the_dice()

# Pass to the next player



# Core function that runs the round and asks the user if wants to roll again or pass the turn

def roll_or_pass(player_choice):
    if player_choice.lower() == "yes" or "y":
        return roll_the_dice()
    elif player_choice.lower() == "no" or "n":
        pass