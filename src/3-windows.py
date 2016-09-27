#!/usr/bin/python

import curses
from curses import wrapper

def make_window(screen):
    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)
    win.clear()

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        win.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
        win.refresh()
        win.getkey()
    win.refresh()

def main():
    wrapper(make_window)
