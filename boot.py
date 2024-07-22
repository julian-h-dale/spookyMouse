import storage 
import usb_cdc
import digitalio
import board
import time

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)
ext_led = digitalio.DigitalInOut(board.GP14)
ext_led.direction = digitalio.Direction.OUTPUT

if button.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    ext_led.value=True
    time.sleep(0.5)
    ext_led.value=False
    time.sleep(0.5)
    ext_led.value=True
