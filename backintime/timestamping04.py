#!/usr/bin/python3

"""
Author: Michael O'Keefe

program to determing time delta to birthday
"""

import datetime as dt

def main():
    """main function"""

    currenttime=dt.datetime.now()            # get current time as currenttime
    print(currenttime)                       # show value of currenttime
    bday=dt.datetime(1968, 8, 22, 12, 0, 0)  # set birthday in bday as 8/22/1968 at noon
    print(bday)                              # show value of bday
    print("delta: ",currenttime-bday)        # show difference between currenttime and bday

if __name__ == '__main__':
    main()
