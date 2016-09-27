#!/usr/bin/python

#source: https://docs.python.org/3/howto/curses.html

import curses # Seven hells!

def setup_curses():
    stdscr = curses.initscr() # initscr() returns a window object representing the entire screen
    curses.noecho() # don't echo pressed keys
    curses.cbreak() # react to keys instantly, without requiring the Enter key to be pressed
    stdscr.keypad(True) #curses handles special keys
    return stdscr

def end_curses(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

def main():
    stdscreen = setup_curses()
    end_curses(stdscreen)
