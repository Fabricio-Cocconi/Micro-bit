calificacion = 0

def on_button_pressed_ab():
    global calificacion
    basic.show_leds("""
        . # # # #
        . . . . #
        . . # # #
        . . . . .
        . . # . .
        """)
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
    calificacion = randint(0, 100)
    basic.show_number(calificacion)
    basic.pause(1000)
    if calificacion >= 75:
        basic.show_leds("""
            # # . # #
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            """)
        basic.pause(1000)
        basic.clear_screen()
        basic.pause(1000)
    basic.show_leds("""
        # # . # #
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
