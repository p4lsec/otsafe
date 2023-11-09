"""
This class is designed to represent a Safety Instrumented System.  It has a name, a value, a unit, and a percentage.
"""

from datetime import datetime
from time import sleep

from otsafe.components.generic import Component
from otsafe.components.alarms import Alarm


class SIS(Component):

    def __init__(
        self,
        name: str,
        value: int  = None,
        unit: str = "",
        **kwargs
    ):
        super().__init__(name) 
        self.name = name
        self.value: int | str = value
        self.unit: str = unit
        self.__dict__.update(kwargs)
        self.last_updated: datetime = datetime.now()
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)
        

    def set_min_alarm(self, value) -> None:
        """
        Sets the minimum alarm value for the sensor.  If the sensor value is less than or equal to this value, the alarm will be triggered.
        """

        self.min_alarm_value = value
        if self.value <= value:
            self.min_alarm.raise_alarm("Min alarm SIS triggered!")

    
    def set_max_alarm(self, value) -> None:
        """
        Sets the maximum alarm value for the sensor.  If the sensor value is greater than or equal to this value, the alarm will be triggered.
        """

        self.max_alarm_value = value
        if self.value >= value:
            self.max_alarm.raise_alarm("Max alarm SIS triggered!")

    
    def raise_alarm(self, message) -> None:
        """
        Raises the alarm.
        """

        return Alarm(alarm=True, name = self.name, message=message)


    def run(self, interval: int = 1, check: bool = False) -> None:
        """
        Runs the SIS.  This is the main loop of the SIS.
        """

        if check:
            if self.value <= self.min_alarm_value:
                self.raise_alarm("Min alarm SIS triggered!")
            elif self.value >= self.max_alarm_value:
                self.raise_alarm("Max alarm SIS triggered!")
            else:
                return("SIS operating nominally.")

        while True:
            self.set_min_alarm(self.min_alarm_value)
            self.set_max_alarm(self.max_alarm_value)
            sleep(interval)


    def read(self) -> str:
        return f"{self.value}{self.unit}"
    

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