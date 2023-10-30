import curses

espera = ['-', '\\', '|', '/']

def main(w):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    alto, ancho = w.getmaxyx()
    w.addstr(alto - 1, 0, "Línea con color invertido", curses.A_REVERSE)
    w.refresh()

    curses.curs_set(False)
    w.addstr(0, 2, "Esperando...")
    for i in range(20):
        w.addstr(0, 0, espera[i%4])
        w.refresh()
        curses.napms(100)

    w.addstr(0, 0, "✓ Hecho!\n", curses.color_pair(1) | curses.A_BOLD)

    curses.curs_set(True)

    w.addstr(1, 0, "Presioná una tecla para probar getch...\n", curses.color_pair(2))
    c = w.getch()
    w.addstr(2, 0, f"Presionaste {chr(c)} ({c})\n")

    w.addstr(1, 0, "Presioná otra para probar getkey...\n", curses.color_pair(2))
    c = w.getkey()
    w.addstr(2, 0, f"Presionaste {c}")

    w.addstr(1, 0, "Presioná otra para ver un pad...\n")

    pad = curses.newpad(100, 100)
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x, ord('a') + (x*x+y*y) % 26)
    pad.refresh( 0,0, 5,5, 20,75)

    w.addstr(1, 0, "Presioná otra para terminar...\n")
    w.getkey()

curses.wrapper(main)


# Cosas a probar:
# begin_x = 20; begin_y = 7
# height = 5; width = 40
# win = curses.newwin(height, width, begin_y, begin_x)
# Note that the coordinate system used in curses is unusual. Coordinates are always passed in the order y,x, and the top-left corner of a window is coordinate (0,0).

# Your application can determine the size of the screen by using the curses.LINES and curses.COLS variables to obtain the y and x sizes. Legal coordinates will then extend from (0,0) to (curses.LINES - 1, curses.COLS - 1).



# A pad is a special case of a window; it can be larger than the actual display screen, and only a portion of the pad displayed at a time. Creating a pad requires the pad’s height and width, while refreshing a pad requires giving the coordinates of the on-screen area where a subsection of the pad will be displayed.

# pad = curses.newpad(100, 100)
# # These loops fill the pad with letters; addch() is
# # explained in the next section
# for y in range(0, 99):
#     for x in range(0, 99):
#         pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
#
# # Displays a section of the pad in the middle of the screen.
# # (0,0) : coordinate of upper-left corner of pad area to display.
# # (5,5) : coordinate of upper-left corner of window area to be filled
# #         with pad content.
# # (20, 75) : coordinate of lower-right corner of window area to be
# #          : filled with pad content.
# pad.refresh( 0,0, 5,5, 20,75)


# Read a string
# s = stdscr.getstr(0, 0, 15)
