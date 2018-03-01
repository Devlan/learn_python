# coding: utf-8
import random
def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while number > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers -= 1
    return points
