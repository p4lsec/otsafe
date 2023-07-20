"""
This class is designed to represent a sensor in the system.  It has a name, a value, a unit, and a percentage.  The unit is a string that represents the units of the sensor's value.  For example, if the sensor's value is 100, and the unit is " psi", then the sensor's value is 100 psi.  If the sensor's value is 100, and the unit is "lbs", then the sensor's value is 100lbs.  The percentage is a float between 0 and 1.  This is used in the get_random_value() method to simulate a sensor whose readings will randomly vary by a given percentage

Calling the read() method returns the sensor's value as a string.  If the sensor's unit is "", then the value is returned as a string.  If the sensor's unit is not "", then the value is returned as a string with the unit appended to the end.  For example, if the sensor's value is 100, and the unit is " psi", then the sensor's value is returned as "100 psi".  If the sensor's value is 100, and the unit is "lbs", then the sensor's value is returned as "100lbs".

Calling the get_random_value() method allows you to simulate a sensor whose readings vary by a given percentage, in both directions.  The percentage is given as a float between 0 and 1. For example, a percentage of 0.1 means that the sensor's readings will vary by +/- 10%. The percentage is the same for all readings.  The sensor's readings will vary by the same percentage in both directions.  For example, if the sensor's reading is 100, and the percentage is 0.1, then the sensor's reading will vary between 90 and 110.

Calling the change_value_over_time() method allows you to simulate a sensor whose readings vary by a given percentage, in both directions.  The percentage is given as a float between 0 and 1. For example, a percentage of 0.1 means that the sensor's readings will vary by +/- 10%. The percentage is the same for all readings.  The sensor's readings will vary by the same percentage in both directions.  For example, if the sensor's reading is 100, and the percentage is 0.1, then the sensor's reading will vary between 90 and 110.
"""

from datetime import datetime
from random import random
from time import sleep

from components.generic import Component


class Sensor(Component):

    def __init__(
        self,
        name: str,
        value: int | str = None,
        unit: str = "",
        **kwargs
    ):
        super().__init__(name) 
        self.value: int | str = value
        self.unit: str = unit
        self.__dict__.update(kwargs)
        self.last_updated: datetime = datetime.now()
        

    def read(self) -> int | str:
        if self.unit == "":
            return self.value
        else:
            return f"{self.value}{self.unit}"

    def noisy_read(self, percentage: float) -> int:
        return self.value * (
            1 + (random() * percentage * 2 - percentage)
        )  # math was recommended by Copilot, hope it works!  Seems ok at a glance but I'm no mathmagician.  -Jace

    def change_value_over_time(self, value: int, seconds: int):
        """
        Changes the value of the sensor over time.  The value is changed by 1 every second until the desired value is reached.  Returns the new value.
        """
          
        if value > self.value:
            while self.value < value:
                self.value += 1
                sleep(seconds)
        elif value < self.value:
            while self.value > value:
                self.value -= 1
                sleep(seconds)
        else:
            self.value

        self.last_updated = datetime.now()

        return self.value