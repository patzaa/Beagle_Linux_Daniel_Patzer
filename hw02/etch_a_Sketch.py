#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time 
import curses

print("----------------------------------------------------------------------------------------------")
print("This is a simple etch-a-sketch program for Homework 2.")
print("Please enter a single number for the horizontal and vertical grid size (size 5-30 recommended)")
print("Use the four push buttons to change the current position")
print("Button 1 moves up, Button 2 moves down, Button 3 moves left, Button 4 moves right")
print("c clears the etch-a-sketch and q is used to quit")
print("----------------------------------------------------------------------------------------------")
GRID_SIZE = int(input("size: ")) #the etch_a_sketch dimensions will be size x size

#GPIOs
Button1 = "P9_18"
Button2 = "P9_20"
Button3 = "P9_22"
Button4 = "P9_24"

#Set the GPIO pins:
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)

SPACING = 1 #Spacing between etch-a-sketch characters
stdscr = curses.initscr() #Initialization for the curses import
curses.noecho()
curses.cbreak()

position_x=3 #Keeps track of user position during game
position_y=3
xnum = 1 #Used for the etch-a-sketch boundaries
ynum = 1

stdscr.addstr(position_y,position_x,'X') #Used to add an X to current position
playGame=True #True until the user quits the game

#Detect button pushes and change curser position accordingly
def updateFunktion(channel):
        global Button1
        global Button2
        global Button3
        global Button4
        global ynum
        global xnum
        global GRID_SIZE
        global position_y
        global position_x

		time.sleep(0.03)

        if channel == Button1:
                if ynum!=1:
                        position_y = position_y - SPACING
                        stdscr.addstr(position_y, position_x, "X")
                        stdscr.refresh()
                        ynum=ynum-1

        elif channel == Button2:
                if ynum != GRID_SIZE:
                        position_y=position_y+SPACING
                        stdscr.addstr(position_y, position_x, "X")
                        ynum=ynum+1
                        stdscr.refresh()

        elif channel == Button3:
                if xnum != 1:
                        position_x=position_x-SPACING
                        stdscr.addstr(position_y, position_x, "X")
                        xnum = xnum-1
                        stdscr.refresh()

        elif channel == Button4:
                if xnum!=GRID_SIZE:
                        position_x=position_x + SPACING
                        stdscr.addstr(position_y, position_x, "X")
                        stdscr.refresh()
                        xnum=xnum+1
        time.sleep(0.03)

print("Programm running...")

#GPIO callback trigger RISING 
GPIO.add_event_detect(Button1, GPIO.RISING, callback=updateFunktion)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=updateFunktion)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=updateFunktion)
GPIO.add_event_detect(Button4, GPIO.RISING, callback=updateFunktion)

#helper functions
try:
        while playGame:
                c=stdscr.getch() #Get keyboard input continiously 

                if c== ord('q'): #q Pressed 

                        playGame=False

                elif c== ord('c'): #c Pressed
                        
					    stdscr.clear()
                        position_x=0
                        position_y=0
                        xnum=1
                        ynum=1
                        stdscr.addstr(position_y, position_x, "X")

except KeyboardInterrupt:
        print("Cleaning Up")
        GPIO.cleanup()

curses.endwin()
