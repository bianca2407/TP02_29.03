ex 1
def on_forever():
    basic.show_string("Bianca")
    basic.clear_screen()
basic.forever(on_forever)

ex 2 
def on_forever():
    led.toggle(2, 3)
basic.forever(on_forever)

ex 3
def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)


ex 4 
def on_forever():
    for index in range(10):
        if index % 2 == 0:
            basic.show_number(index)
basic.forever(on_forever)


ex 5
index = 0
for index2 in range(9):
    if index % 2 == 1:
        basic.show_number(index)
        index += 1

ex 6
i = 0
j = 0
def on_button_pressed_a():
    global i, j
    i = 1
    j = 0
    while j >= 0:
        while i >= 1:
            led.toggle(i, j)
            i += 1
        j += 1
input.on_button_pressed(Button.A, on_button_pressed_a)
