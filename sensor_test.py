import time as time
import RPi.GPIO as GPIO

#Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

#Right 10cm sensor
GPIO.setup(6, GPIO.IN)

#Left 10cm sensor
GPIO.setup(5, GPIO.IN)

#Right 5cm sensor
GPIO.setup(15, GPIO.IN)

#Left 5cm sensor
GPIO.setup(14, GPIO.IN)

#Front 10cm sensor
GPIO.setup(18, GPIO.IN)

print ('Front sensor')
print (GPIO.input(18))

print ('Right 5cm sensor')
print (GPIO.input(15))

print ('Right 10cm sensor')
print (GPIO.input(6))

print ('Left 5cm sensor')
print (GPIO.input(14))

print ('Left 10cm sensor')
print (GPIO.input(5))

