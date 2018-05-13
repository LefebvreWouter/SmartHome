import RPi.GPIO as GPIO
import time

pir_sensor = 18
servo = 23


GPIO.setmode(GPIO.BCM)

GPIO.setup(servo,GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)

p = GPIO.PWM(23,50)

p.start(7.5)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(servo,1)
            p.ChangeDutyCycle(7.5)
            time.sleep(5)
            print("pir wacht")
            GPIO.output(servo, 1)
            p.ChangeDutyCycle(12.5)
            time.sleep(30)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()