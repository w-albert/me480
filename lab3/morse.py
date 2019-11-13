import board
import digitalio
import time
 
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
 
unit = 0.25 

while True:
    # D
    led.value = True
    time.sleep(3*unit)
    led.value = False
    time.sleep(unit)
    led.value = True
    time.sleep(unit)
    led.value = False
    time.sleep(unit)
    led.value = True
    time.sleep(unit)
    led.value = False
    time.sleep(3*unit)
    # O
    led.value = True
    time.sleep(3*unit)
    led.value = False
    time.sleep(unit)
    led.value = True
    time.sleep(3*unit)
    led.value = False
    time.sleep(unit)
    led.value = True
    time.sleep(3*unit)
    led.value = False
    time.sleep(3*unit)
    # T
    led.value = True
    time.sleep(3*unit)
    led.value = False
    time.sleep(7*unit)