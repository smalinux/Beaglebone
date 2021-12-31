# Google: set_duty_cycle python
import Adafruit_BBIO.PWM as PWM

# setup PINs
myPWM = "P8_13"

PWM.start(myPWM, 0, 1000)

while True:
    duty = input("what duty cycle would you like: ")
    PWM.set_duty_cycle(myPWM, int(duty));

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
