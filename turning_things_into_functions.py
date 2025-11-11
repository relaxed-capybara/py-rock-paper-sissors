import pygame


def fadingEfect(FadingItem1, FadingItem2, game_state):
    game_state.timer += 1 / 60
    FadingItem1.set_alpha(max(0, 255 - (game_state.timer / 1.5 * 255)))
    FadingItem2.set_alpha(max(0, 255 - (game_state.timer / 1.5 * 255)))
    game_state.fade_alpha = int(max(0, 255 - (game_state.timer / 1.5 * 255)))

    if game_state.timer >= 1.5:
        FadingItem1.set_alpha(0)
        FadingItem2.set_alpha(0)
        game_state.timer = 0
        game_state.fading_active = False


def activator(index_, game_state, FadingItem1, FadingItem2, event):
    if event.key == pygame.K_SPACE and game_state.selected_item == index_ and (game_state.timer == 0 or game_state.timer >= 1.5):
        game_state.timer = 0
        game_state.fading_active = True
        game_state.index_ = index_
        game_state.locked = True


def handle_fade(index, FadingItem1, FadingItem2, game_state):
    """Call this every frame in the main loop to handle fading."""
    if game_state.fading_active:

        if game_state.index_ == 0:
            fadingEfect(game_state.lovly_paper,
                        game_state.lovly_sissors, game_state)

        if game_state.index_ == 1:
            fadingEfect(game_state.lovly_stone,
                        game_state.lovly_sissors, game_state)

        if game_state.index_ == 2:
            fadingEfect(game_state.lovly_paper,
                        game_state.lovly_stone, game_state)
