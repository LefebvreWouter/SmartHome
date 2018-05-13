import RPi.GPIO as GPIO
import time
import mysql.connector as mc

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 5
led2 =6
led3 = 13
alleLeds=[led1,led2,led3]

Button = 26



GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.setup(Button, GPIO.IN, GPIO.PUD_UP)




while True:

    while GPIO.input(Button) == True:
        print("licht is aan ")
        GPIO.output(alleLeds, 1)
        GPIO.output(alleLeds, 1)
        # time.sleep(1)
        GPIO.output(alleLeds, 1)
        # time.sleep(1)
        GPIO.output(alleLeds, 1)
        # time.sleep(1)
        connection = mc.connect(host="localhost", user="wouter", passwd="root", db="SmartHome")
        cursor = connection.cursor()
        q1 = "INSERT INTO LED(Meting, MetingInterval, Datum, Uur, HuisId, SensorSerieNr) VALUES(" + str(led1) + ", 10, curdate(), curtime(), 1, '12UYT89')"
        cursor.execute(q1)
        connection.commit()

    else:
        if GPIO.input(Button) == True:
            GPIO.output(alleLeds,0)
            time.sleep(1)
            print("licht is uit")


GPIO.cleanup()





# import RPi.GPIO as GPIO
# import time
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#
# led = 5
# button = 6
#
# GPIO.setup(led, GPIO.OUT)
# GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
#
# while True:
#
#     if GPIO.input(button) == True:
#
#         GPIO.output(led, 1)
#         time.sleep(1)
#         GPIO.output(led, 0)
#         time.sleep(1)
#         GPIO.output(led, 1)
#         time.sleep(1)
#         GPIO.output(led, 0)
#         time.sleep(1)
# GPIO.cleanup()
#