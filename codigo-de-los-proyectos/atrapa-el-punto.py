def on_button_pressed_a():
    if contador.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
    else:
        game.game_over()
input.on_button_pressed(Button.A, on_button_pressed_a)

contador: game.LedSprite = None
contador = game.create_sprite(2, 2)

def on_forever():
    contador.move(1)
    basic.pause(100)
    contador.if_on_edge_bounce()
basic.forever(on_forever)
