import RPi.GPIO as GPIO
from time import sleep
# 6, 13, 19, 26

lf_pin = 19
rf_pin = 13
rb_pin = 6
lb_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(lf_pin, GPIO.OUT)
GPIO.setup(rf_pin, GPIO.OUT)
GPIO.setup(rb_pin, GPIO.OUT)
GPIO.setup(lb_pin, GPIO.OUT)

def lf():
    GPIO.output(lf_pin, GPIO.HIGH)

def rf():
    GPIO.output(rf_pin, GPIO.HIGH)

def rb():
    GPIO.output(rb_pin, GPIO.HIGH)

def lb():
    GPIO.output(lb_pin, GPIO.HIGH)



import curses
arrow_key = curses.initscr().getch()
try:
    while True:

        if arrow_key == curses.KEY_UP:
            lf()
            rf()
        elif arrow_key == curses.KEY_DOWN:
            rb()
            lb()
        elif arrow_key == curses.KEY_RIGHT:
            rf()
            lb()
        elif arrow_key == curses.KEY_LEFT:
            lf()
            rb()
        else:
            sleep(1)
            print("Not an arrow key")
finally:
    GPIO.cleanup()