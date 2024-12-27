# Configuración de eventos

def on_button_pressed_a():
    global cursor_x
    cursor_x = (cursor_x - 1) % 5
    draw_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def game_loop():
    while True:
        check_collision()
        basic.pause(100)

def on_button_pressed_ab():
    global cursor_y
    cursor_y = (cursor_y + 1) % 5
    draw_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global cursor_x
    cursor_x = (cursor_x + 1) % 5
    draw_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

# Función para mostrar la pantalla
def draw_screen():
    basic.clear_screen()
    led.plot(star_x, star_y)
    # Dibuja la estrella
    led.plot(cursor_x, cursor_y)
# Dibuja el cursor
# Botón A mueve el cursor hacia la izquierda
# Botón B mueve el cursor hacia la derecha
# Botón AB mueve el cursor hacia abajo
# Actualiza la estrella y puntuación cuando el cursor la atrapa
def check_collision():
    global score, star_x, star_y
    if cursor_x == star_x and cursor_y == star_y:
        score += 1
        basic.show_string("Score: " + ("" + str(score)))
        star_x = Math.random_range(0, 4)
        star_y = Math.random_range(0, 4)
        draw_screen()
score = 0
star_y = 0
star_x = 0
cursor_y = 0
cursor_x = 0
cursor_x = 2
cursor_y = 2
# Juego principal
draw_screen()
game_loop()