from turtle import *

speed(0)

def levy(n):
    l=4
    if n == 0:
        forward(20)
    else:
         left(45)
         levy(n - 1)
         right(45)
         right(45)
         levy(n-1)
         left(45)

levy(8)
