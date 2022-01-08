# Google: set_duty_cycle python
import Adafruit_BBIO.PWM as PWM
from time import sleep

# setup PINs
myPWM = "P8_13"

PWM.start(myPWM, 0, 1000)

while 1:
    for x in range(1, 100):
        sleep(0.05)
        print(x);
        PWM.set_duty_cycle(myPWM, x)
    y = 100;
    while y >=0:
        sleep(0.05)
        print(y);
        PWM.set_duty_cycle(myPWM, y)
        y -=1

PWM.stop(myPWM)
PWM.cleanup()
    
# setup my voltage:
"""
while True:
    v = input("what duty volt would you like: ")
    duty = v/3.365*100
    if duty > 100:
        duty=100
    PWM.set_duty_cycle(myPWM, int(duty));
"""
