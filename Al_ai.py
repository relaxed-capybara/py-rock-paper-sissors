import random
# al random picking
last_number = None


def random_less_repeats():
    global last_number
    new_number = random.randint(0, 2)
    if new_number == last_number:
        new_number = random.randint(0, 2)
    last_number = new_number
    return new_number


enemy_choice = random_less_repeats()


def grading_score(game_state):
    if game_state.locked == True:
        if enemy_choice == 0 and game_state.selected_item == 0:  # tie
            game_state.wins += 1
        if enemy_choice == 0 and game_state.selected_item == 1:  # lost
            game_state.loses += 1
        if enemy_choice == 0 and game_state.selected_item == 2:  # won
            game_state.ties += 1

        if enemy_choice == 1 and game_state.selected_item == 0:  # lost
            game_state.loses += 1
        if enemy_choice == 1 and game_state.selected_item == 1:  # tie
            game_state.ties += 1
        if enemy_choice == 1 and game_state.selected_item == 2:  # won
            game_state.wins += 1

        if enemy_choice == 2 and game_state.selected_item == 0:  # won
            game_state.wins += 1
        if enemy_choice == 2 and game_state.selected_item == 1:  # tie
            game_state.ties += 1
        if enemy_choice == 2 and game_state.selected_item == 2:  # lost
            game_state.loses += 1


def making_next_round(game_state):
    game_state.fade_alpha = 255
    game_state.lovly_sissors.set_alpha(255)
    game_state.lovly_paper.set_alpha(255)
    game_state.lovly_stone.set_alpha(255)
    game_state.locked = False


def enemies_choose(game_state):
    global enemies_choice
