from guizero import App, Text, PushButton
from gpiozero import TrafficLights

lights = TrafficLights(22, 27, 17)

app = App()

PushButton(app, command=lights.red.on, text="on")

app.display()

app = App("Traffic Lights controller", layout="grid")

Text(app, "Red", grid=[0, 0])
PushButton(app, command=lights.red.on, text="on", grid=[1, 0])
PushButton(app, command=lights.red.off, text="off", grid=[2, 0])

# Try adding all three Lights
