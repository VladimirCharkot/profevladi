from turtle import *

def figura(n):
    for i in range(n):
        forward(100)
        left(360/n)

# def flor(cant_fig, cant_lados):
#   ...

for i in range(8):
    figura(6)
    left(45)


