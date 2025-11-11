import random
state = game_state
# al random picking
last_number = None


def random_less_repeats():
    global last_number
    new_number = random.randint(0, 2)
    if new_number == last_number:
        new_number = random.randint(0, 2)
    last_number = new_number
    return new_number


if state.locked == True:
    def grading_score(game_state):
        if random_less_repeats == 0 and game_state.selected_item == 0:  # tie
            game_state.wins += 1
        if random_less_repeats == 0 and game_state.selected_item == 1:  # lost
            game_state.loses += 1
        if random_less_repeats == 0 and game_state.selected_item == 2:  # won
            game_state.ties += 1

        if random_less_repeats == 1 and game_state.selected_item == 0:  # lost
            game_state.loses += 1
        if random_less_repeats == 1 and game_state.selected_item == 1:  # tie
            game_state.ties += 1
        if random_less_repeats == 1 and game_state.selected_item == 2:  # won
            game_state.wins += 1

        if random_less_repeats == 2 and game_state.selected_item == 0:  # won
            game_state.wins += 1
        if random_less_repeats == 2 and game_state.selected_item == 1:  # tie
            game_state.ties += 1
        if random_less_repeats == 2 and game_state.selected_item == 2:  # lost
            game_state.loses += 1
