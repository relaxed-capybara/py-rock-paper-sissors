from core_helpers import pick_cpu_choice
from core_types import GameChoice


def fadingEfect(FadingItem1, FadingItem2, game_state):
    game_state.timer += 1 / 60
    FadingItem1.set_alpha(max(0, 255 - (game_state.timer / 1.5 * 255)))
    FadingItem2.set_alpha(max(0, 255 - (game_state.timer / 1.5 * 255)))
    game_state.fade_alpha = (max(0, 255 - (game_state.timer / 1.5 * 255)))
    game_state.enemy_alpha = (max(0, 255 - (game_state.timer / 1.5 * 255)))

    if game_state.timer >= 1.5:
        FadingItem1.set_alpha(0)
        FadingItem2.set_alpha(0)
        game_state.timer = 0
        game_state.fading_active = False
        game_state.enemy_alpha = 0


def activator(game_state):
    game_state.timer = 0
    game_state.fading_active = True
    game_state.locked = True
    game_state.cpu_choice = pick_cpu_choice()

    print(f"CPU chose {game_state.cpu_choice}")


def handle_fade(game_state):
    """Call this every frame in the main loop to handle fading."""
    if game_state.fading_active:

        if game_state.selected_item == GameChoice.Rock:
            fadingEfect(game_state.lovly_paper,
                        game_state.lovly_sissors, game_state)

        if game_state.selected_item == GameChoice.Paper:
            fadingEfect(game_state.lovly_stone,
                        game_state.lovly_sissors, game_state)

        if game_state.selected_item == GameChoice.Sissors:
            fadingEfect(game_state.lovly_paper,
                        game_state.lovly_stone, game_state)


def change_icon(game_state):
    if game_state.accu == "rock":
        game_state.accu = "paper"
        game_state.timerAL = 0
    elif game_state.accu == "paper":
        game_state.accu = "sissors"
        game_state.timerAL = 0
    else:
        game_state.accu = "rock"
        game_state.timerAL = 0


def draw_icon(game_state):
    if game_state.cpu_choice is not None:
        img = game_state.cpu_asset_for_choice()
        game_state.screen.blit(img, dest=(
            game_state.margin + game_state.asset_width + game_state.space_between, 100))
        return

    if game_state.accu == "rock":
        game_state.screen.blit(game_state.stone, dest=(
            game_state.margin + game_state.asset_width + game_state.space_between, 100))
    elif game_state.accu == "paper":
        game_state.screen.blit(game_state.paper, dest=(
            game_state.margin + game_state.asset_width + game_state.space_between, 100))
    elif game_state.accu == "sissors":
        game_state.screen.blit(game_state.sissors, dest=(
            game_state.margin + game_state.asset_width + game_state.space_between, 100))


def draw_tex(text, font, text_color, x, y, game_state):
    img = font.render(text, True, text_color)
    game_state.screen.blit(text, x, y)
