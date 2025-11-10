timer = 0

def fadingEfect(FadingItem1, FadingItem2):
    timer = 0
    
    timerStart += 1 / 60
    FadingItem1.set_alpha(max(0, 255 - (timer / 1.5 * 255)))
    FadingItem2.set_alpha(max(0, 255 - (timer / 1.5 * 255)))
    fade_alpha = int(max(0, 255 - (timer / 1.5 * 255)))
    if timer >= 1.5:
        FadingItem1.set_alpha(0)
        FadingItem2.set_alpha(0)

def activator(index_,FadingItem1, FadingItem2 ):
    if event.key == pygame.K_SPACE and selected_item == index_ and (timer == 0 or timer >= 1.5):
        timer = 0
        fadingEfect(FadingItem1, FadingItem2)
        #locked = True

