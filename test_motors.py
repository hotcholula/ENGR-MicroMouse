import time as time
import RPi.GPIO as GPIO

#Set GIIO pin numbering
GPIO.setmode(GPIO.BCM)

#Initial right side pins
GPIO.setup(27, GPIO.OUT) #1EN
GPIO.setup(2, GPIO.OUT) #1A
GPIO.setup(3, GPIO.OUT) #1B

#Initial left side pins
GPIO.setup(22, GPIO.OUT) #2EN
GPIO.setup(4, GPIO.OUT) #2A
GPIO.setup(17, GPIO.OUT) #2B

#Move Forward
GPIO.output(27,1)
GPIO.output(2,1)
GPIO.output(3,0)
GPIO.output(22,1)
GPIO.output(4,0)
GPIO.output(17,1)
time.sleep(2)
GPIO.output(27,0)
GPIO.output(6,0)
GPIO.output(3,0)
GPIO.output(22,0)
GPIO.output(9,0)
GPIO.output(17,0)

time.sleep(2)

#Move Reverse
GPIO.output(27,1)
GPIO.output(2,0)
GPIO.output(3,1)
GPIO.output(22,1)
GPIO.output(4,1)
GPIO.output(17,0)
time.sleep(2)
GPIO.output(27,0)
GPIO.output(2,0)
GPIO.output(3,0)
GPIO.output(22,0)
GPIO.output(4,0)
GPIO.output(17,0)

time.sleep(0.2)

#Move Left
GPIO.output(27,1)
GPIO.output(2,0)
GPIO.output(3,1)
GPIO.output(22,1)
GPIO.output(4,0)
GPIO.output(17,1)
time.sleep(2)
GPIO.output(27,0)
GPIO.output(2,0)
GPIO.output(3,0)
GPIO.output(22,0)
GPIO.output(4,0)
GPIO.output(17,0)

time.sleep(0.2)

#Move Right
GPIO.output(27,1)
GPIO.output(2,1)
GPIO.output(3,0)
GPIO.output(22,1)
GPIO.output(4,1)
GPIO.output(17,0)
time.sleep(2)
GPIO.output(27,0)
GPIO.output(2,0)
GPIO.output(3,0)
GPIO.output(22,0)
GPIO.output(4,0)
GPIO.output(17,0)
