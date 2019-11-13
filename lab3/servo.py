import board
import time
import pulseio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm,min_pulse=500,max_pulse=2400)

while True:
    for angle in range(0, 45, 15): # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.5)
    for angle in range(45, 15, -5): # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)
    for angle in range(15, 90, 15): # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.25)    
    for angle in range(90, 0, -10): # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.5)
    time.sleep(2)