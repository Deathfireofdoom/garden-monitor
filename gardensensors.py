import sys
import adafruit_dht
import RPi.GPIO as GPIO


class GardenSensor():
    def __init__(self) -> None:
        dht = adafruit_dht.DHT11(4)
        self.temp_value = dht.temperature
        self.hum_value = dht.humidity

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.IN)
        self.soil_value = GPIO.input(14)
    
    @property
    def all(self):
        return {'hum': self.hum_value, 
                'temp': self.temp_value,
                'soil': self.soil_value}

    @property
    def temp(self):
        return {'temp': self.temp_value}
    
    @property
    def hum(self):
        return {'hum': self.hum_value}

    @property
    def soil(self):
        return {'soil': self.hum_value}
    
    def save(self):
        pass
    