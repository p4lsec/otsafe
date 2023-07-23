import datetime
from components.generic import Component


class Actuator(Component):
    def __init__(self, name, open: bool = False):
        super().__init__(name)
        self.open = open
        self.last_modified = datetime.datetime.now()