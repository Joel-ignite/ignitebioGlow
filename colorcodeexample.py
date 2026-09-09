#Example file on how to deploy with color coding 

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

hub = PrimeHub()

color_sensor = ColorSensor(Port.B)

left_motor = Motor(Port.A)
right_motor = Motor(Port.C)


def red_task():
    print("RED TASK")

    left_motor.run(500)
    right_motor.run(500)
    wait(1000)

    left_motor.stop()
    right_motor.stop()


def blue_task():
    print("BLUE TASK")

    left_motor.run(-500)
    right_motor.run(-500)
    wait(1000)

    left_motor.stop()
    right_motor.stop()


def green_task():
    print("GREEN TASK")

    # Do whatever your green task needs.
    wait(1000)


while True:

    color = color_sensor.color()

    if color == Color.RED:
        red_task()

    elif color == Color.BLUE:
        blue_task()

    elif color == Color.GREEN:
        green_task()

    wait(50)
