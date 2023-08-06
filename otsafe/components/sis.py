import os
import time

from components.generic import Component
from components.sensors import Sensor
from components.actuators import Actuator
from components.alarms import Alarm

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

SLEEP = os.getenv('SLEEP', 1)


class SIS(Component):
    def __init__(
            self,
            sensor: Sensor,
            actuator: Actuator
    ):
        self.sensor = sensor
        self.actuator = actuator
        
    def set_min(self, min: int) -> True:
        self.min = min
        return True
    
    def set_max(self, max: int) -> True:
        self.max = max
        return True

    def run(self, check: bool = False, intervene: bool = True) -> None:
        """
        This multifunctional method will run the SIS, either with a single check, or in a continual loop. 

        If check is set to True, this function will peform a single check of values.  Otherwise, it will run in a loop. 
        
        If intervene is set to True, the actuator will be triggered if a sensor value is out of the defined range. Otherwise, an alarm will be raised. 

        The time between loop cycles can be overridden by setting the `SLEEP` value in the .env of the project. 
        """
        while True:

            if self.sensor.value <= self.min:
                message = f"Detected low value of {self.sensor.value} with set point {self.min}"
                if intervene:
                    self.actuator.open()
                raise Alarm(message)
            elif self.sensor.value >= self.max:
                message = f"Detected high value of {self.sensor.value} with set point {self.max}"
                if intervene:
                    self.actuator.close()
                raise Alarm(message)
            
            else:
                if check:
                    return None
                else:
                    time.sleep(SLEEP)
                    continue