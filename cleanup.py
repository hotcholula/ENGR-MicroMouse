import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print ('Cleaned up pins')
gpio_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 28, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
for item in gpio_pins:
     GPIO.setup(item, GPIO.IN)

GPIO.cleanup()
