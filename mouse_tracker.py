#! /usr/bin/env python

from Xlib import display
from math import sqrt
from subprocess import call

def tracker():
    disp = display.Display().screen()
    conv = (disp.width_in_mms / 10) / disp.width_in_pixels
    travelled = 0
    pos = disp.root.query_pointer()._data
    last_x, last_y = pos['root_x'], pos['root_y']
    meters = 0
    while 1:
        pos = disp.root.query_pointer()._data
        if pos['root_x'] != last_x and pos['root_y'] != last_y:
            travelled += abs(last_x - pos['root_x']) * conv
            travelled += abs(last_y - pos['root_y']) * conv
            last_x, last_y = pos['root_x'], pos['root_y']
            if travelled >= 100:
                travelled -= 100
                meters += 1
                if meters == 1:
                    call(['notify-send', 'Mouse Tracker', '1m !'])
                if not meters % 1000:
                    call(['notify-send', 'Mouse Tracker',
                        str(meters / 1000) + 'km !'])
            

if __name__ == '__main__':
    tracker()
