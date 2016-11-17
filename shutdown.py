# shutdown script for Raspberry Pi<br />
# watch LOW level on pin 5 to enter sleep mode<br />
# status led on pin 7: ON = ready, BLINK = confirm button<br />
import RPi.GPIO as GPIO
import os
import time
# use the pin number as on the raspi board<br />
GPIO.setmode(GPIO.BOARD)
# set pin 7 as output and HIGH, pin 5 is input<br />
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)
GPIO.setup(5, GPIO.IN)
# start the loop for every .5 seconds, waiting for LOW on pin 5<br />
# then 2 short flashes with led to confirm and shutdown to sleep mode<br />
while True:
        if not (GPIO.input(5)):
                GPIO.output(7, False)
                time.sleep(.1)
                GPIO.output(7, True)
                time.sleep(.1)
                GPIO.output(7, False)
                time.sleep(.1)
                GPIO.output(7, True)
                os.system("sudo shutdown -h now")
        time.sleep(.5)