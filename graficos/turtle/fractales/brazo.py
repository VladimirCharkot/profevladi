from turtle import *
from math import cos, radians


def brazo(l, a = 15):
    rads = radians(a)
    h = (l/2) / cos(rads)
    left(a)
    forward(h)
    right(2*a)
    forward(h)
    left(a)

