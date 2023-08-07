import datetime
from otsafe.components.generic import Component


class Actuator(Component):
    def __init__(self, name, open: bool = False, **kwargs):
        super().__init__(name)
        self.name = name
        self.open = open
        self.last_modified = datetime.datetime.now()
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)