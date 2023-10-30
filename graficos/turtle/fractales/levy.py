from turtle import *

speed(0)
X, Y = 0, 1

def levy(p1, p2, level):

    def linea(p1, p2):
        penup()
        goto(p1)
        pendown()
        goto(p2)

    if level == 0:
        linea(p1, p2)
    else:
        s = (p1 + p2) * 0.5  # sum / 2
        d = (p1 - p2) * 0.5  # difference / 2

        m = Vec2D(s[X] + d[Y], s[Y] - d[X])

        levy(p1, m, level - 1)
        levy(m, p2, level - 1)

def main():
    level = int(input("Enter the level (0 or greater): "))
    levy(Vec2D(50, -50), Vec2D(50, 50), level)
    #screen.mainloop()

main()
