import curses
import time
import random
import string
from multiprocessing import Process




#randoms curses
stdscr = curses.initscr()

curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)


#def main(stdscr):




def making():
    res = string.printable
    ra = random.choice(res)
    pos = random.randint(0,119)
    stdscr.addstr(0,pos,ra)
    stdscr.refresh()
    time.sleep(2)
    return pos




def updating(pos):
    for i in range(30):
        ra = random.choice(res)
        stdscr.addstr(i,pos,ra)

        if(i > 19):
            stdscr.addstr(i-20,pos," ")

        time.sleep(0.2)
        stdscr.refresh()


for i in range(2):
    making()
    making()
    making()

'''
def updating(ra):

    return sup


while True:
    pos = random.randint(0,119)
    stdscr.addstr(0,pos,ra)
    stdscr.refresh()

    for i in range(30):
        ra = random.choice(res)
        stdscr.addstr(i,pos,ra)

        if(i > 19):
            stdscr.addstr(i-20,pos," ")

        time.sleep(0.2)
        stdscr.refresh()
    break
'''
#curses.wrapper(main)


curses.curs_set(1)
curses.noecho()
curses.cbreak()
stdscr.keypad(False)

curses.endwin()
