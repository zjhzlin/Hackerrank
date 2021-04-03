#
import math
import os
import random
import re
import sys

class Car(object):
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit

    def __str__(self):
        # return "Car"
        return "Car with the maximum speed of " + str(self.max_speed) + " " + self.speed_unit


class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return "Boat with the maximum speed of " + str(self.max_speed) + " knots"


if __name__ == '__main__':
    print('ok')
    car = Car(100, 'km/h')
    print(car)
