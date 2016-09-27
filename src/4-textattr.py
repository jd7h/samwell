#!/usr/bin/python

import curses # Duizend bommen en granaten
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    line = 0
    for att in [curses.A_BLINK,
                curses.A_BOLD,
                curses.A_DIM,
                curses.A_REVERSE,
                curses.A_STANDOUT,
                curses.A_UNDERLINE]:
        stdscr.addstr(line, 0, "Greetings earthling!",att)
        stdscr.refresh()
        line += 1
        stdscr.getkey()

    if curses.has_colors():
        for color in range(1,8):
            curses.init_pair(color, color, curses.COLOR_WHITE)
            stdscr.addstr(line, 0, "TASTE THE RAINBOW", curses.color_pair(color))
            stdscr.refresh()
            line += 1
            stdscr.getkey()

wrapper(main)
