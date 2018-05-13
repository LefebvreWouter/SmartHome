import spidev
import mysql.connector as mc
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)



# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)



def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

#weerstand kan nooit
def ConvertTemp(data, places):
    temp = ((data) / float(1023)) * 330
    temp = round(temp, places)
    return temp


#sensor kanaal
light_channel = 0
temp_channel = 1
delay = 10

while True:
    connection = mc.connect(host="localhost", user="wouter", passwd="root", db="SmartHome")
    cursor = connection.cursor()
    # leest licht kanaal
    light_level = ReadChannel(light_channel)
    light_volts = ConvertVolts(light_level, 2)
    q1 = "INSERT INTO Licht(Meting, MetingInterval, Datum, Uur, HuisId, SensorSerieNr) VALUES(" + str(light_level) + ", 60, curdate(), curtime(), 1, 'GH678VT906')"
    cursor.execute(q1)
    connection.commit()
    # leest temp
    temp_level = ReadChannel(temp_channel)
    temp_volts = ConvertVolts(temp_level, 2)
    temp = ConvertTemp(temp_level, 2)
    q2 = "INSERT INTO Temperatuur(Meting, MetingInterval, Datum, Uur, HuisId, SensorSerieNr) VALUES(" + str(temp) + ", 60, curdate(), curtime(), 1, 'AB6579VC456')"
    cursor.execute(q2)
    connection.commit()

    print(
    "--------------------------------------------")
    print("Light: {} ({}V)".format(light_level, light_volts))
    print("Temp : {}  {} deg C".format(temp_level, temp))


    time.sleep(delay)
    connection.close()

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(23)
    if input_state == False:
        print ("Light: {} ".format(light_level))
        time.sleep(1)
    else:
        print ("Temp : {} deg C".format(temp))

    time.sleep(delay)