import RPi.GPIO as GPIO
import time

pir_sensor = 25
servo = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)
GPIO.setup(pir_sensor, GPIO.IN)
GPIO.PWM(23,50)
pulse = (7.5)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(servo,1)
            pulse.ChangeDutyCycle(7.5)
            time.sleep(5)
            print("pir wacht")
            GPIO.output(servo, 1)
            pulse.ChangeDutyCycle(12.5)
            time.sleep(5)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()