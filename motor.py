import time
import RPi.gpio as gpio

motorA1 = 16
motorA2 = 18

gpio.setmode(gpio.BOARD)
gpio.setup(motorA1, gpio.out)
gpio.setup(motorA2, gpio.out)

gpio.output(motorA1, gpio.HIGH)
gpio.output(motorA2, gpio.LOW)
time.sleep(5)

gpio.output(motorA1, gpio.LOW)
gpio.output(motorA2, gpio.HIGH)
time.sleep(5)

gpio.cleanup()