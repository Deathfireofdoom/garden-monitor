import sys
import adafruit_dht
import RPi.GPIO as GPIO
from time import sleep


global dht 
dht = adafruit_dht.DHT11(4)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

class GardenSensor():
    def __init__(self) -> None:
        pass


    @property
    def all(self):
        self._update_sensors()
        return {'hum': self.hum_value,
                'temp': self.temp_value,
                'soil': self.soil_value}

    @property
    def temp(self):
        self._update_sensors()
        return {'temp': self.temp_value}
    
    @property
    def hum(self):
        self._update_sensors()
        return {'hum': self.hum_value}

    @property
    def soil(self):
        self._update_sensors()
        return {'soil': self.hum_value}

    def water_plants(self):
        GPIO.output(11, 1)
        sleep(5)
        GPIO.output(11, 0)
    
    def _update_sensors(self):
        self.temp_value = dht.temperature
        self.hum_value = dht.humidity
        self.soil_value = GPIO.input(13)


    def save(self):
        pass
