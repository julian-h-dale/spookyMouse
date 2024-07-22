import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
import random

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ext_led = digitalio.DigitalInOut(board.GP14)
ext_led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

mouse = Mouse(usb_hid.devices)
print("starting the mouse")
print(mouse)

def hitTheLights(on=False):
    led.value = on
    ext_led.value = on

def switchLights():
    led.value = not led.value
    ext_led.value = not ext_led.value

def moveMouse(inverse=1):
    x = random.randint(1,100) * inverse
    y = random.randint(1,100) * inverse
    print("x={} y={}".format(x, y))
    mouse.move(x, y)

def blinkyblink(light):
    for x in range(0,3):
        light.value = not light.value
        time.sleep(0.5)
    

pause = False
while True:
    if button.value:
        pause = not pause
        print("pause set to {}".format(pause))
        ext_led.value = pause
        time.sleep(0.5)
    if pause:
        blinkyblink(ext_led)
    else:
        switchLights()
        moveMouse()
        time.sleep(10)
    