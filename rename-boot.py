import storage 
import usb_cdc
import digitalio
import board

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)


if button.value:
    print("suprresing connection...")
# storage.disable_usb_drive()
# usb_cdc.disable()