from otsafe.components.generic import Component
from otsafe.exceptions import AlarmException

class Alarm(Component):
    def __init__(
            self,
            name: str,
            alarm: bool = False,
            message: str = None,
            **kwargs
    ):
        
        super().__init__(name)
        self.alarm = alarm
        self.message = message

        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)

        if alarm:
            raise AlarmException(self.message)