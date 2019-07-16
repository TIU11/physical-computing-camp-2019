from gpiozero import LED, Button

red = LED(25)
amber = LED(28)
green = LED(27)

button = Button(21)

while True:
    if button.is_pressed:
        green.on()
        amber.on()
        red.on()
    else:
        green.off()
        amber.off()
        red.off()
