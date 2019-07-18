import curses
import time
import random
import string
from multiprocessing import Process

stdscr = curses.initscr()
curses.start_color()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


res = string.printable
ra = random.choice(res)
str_len = range(5,30)

curses.use_default_colors()

while True:
    pos = random.randint(0,119)
    stdscr.addstr(0,pos,ra)
    stdscr.refresh()

    for i in range(30):
        ra = random.choice(res)
        stdscr.addstr(i,pos,ra)

        ran_y = random.randint(2,30)

        if(i > 19):
            stdscr.addstr(i-20,pos," ")

        time.sleep(0.2)
        stdscr.refresh()



curses.curs_set(1)
curses.noecho()
curses.cbreak()
stdscr.keypad(False)

curses.endwin()
