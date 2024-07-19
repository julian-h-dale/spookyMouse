
import neopixel
import board
import usb_hid
import time
import random
from adafruit_hid.mouse import Mouse


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
mouse = Mouse(usb_hid.devices)

# GLOBALS
#x_key = 0
#y_key = 1
delay = 10

def signalRed():
    print("signalRed")
    pixels.fill((255,0,0))


def signalGreen():
    print("signalGreen")
    pixels.fill((0,255,0))

def signalBlue():
    print("signalBlue")
    pixels.fill((0,0,255))

def signalWhite():
    print("signalWhite")
    pixels.fill((255,255,255))

def getRandomCoords():
    x = random.randint(1,200)
    y = random.randint(1,200)
    return (x,y)


def nudgeMouse():
    x, y = getRandomCoords()
    print("x = {} y = {}".format(x, y))
    mouse.move(x = x, y = y)


signalWhite()
time.sleep(5)
while True:
    signalGreen()
    nudgeMouse()
    time.sleep(delay)
    signalRed()
    nudgeMouse()
    time.sleep(delay)

