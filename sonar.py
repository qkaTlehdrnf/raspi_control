import RPi.GPIO as gpio
import time
def measure():
    gpio.output(gpio_TRIGGER, True)
    time.sleep(0.00001)
    gpio.output(gpio_TRIGGER, False)
    start = time.time()
    timeOut = start

    while gpio.input(gpio_ECHO)==0:
        if time.time()-timeOut > 0.0088:
            return -1
    start = time.time()

    while gpio.input(gpio_ECHO)==1:
        if time.time()-start > 0.0088:
            return -1
    stop = time.time()

    elapsed = stop-start
    distance = min(150, (elapsed * 34300)/2)

    return distance

gpio.setmode(gpio.BOARD)
gpio_TRIGGER = 10
gpio_ECHO    = 12
 
gpio.setup(gpio_TRIGGER,gpio.OUT)
gpio.setup(gpio_ECHO,gpio.IN)
gpio.output(gpio_TRIGGER, False)

time.sleep(.1)
while True:
    dis = int(measure())
    print('\r',f'{dis:3d} {"#"*(dis//5)+" "*30}', end=" ")
    time.sleep(0.1)
