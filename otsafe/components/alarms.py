from otsafe.components.generic import Component


class Alarm(Component):
    def __init__(self, name: str, alarm: bool = False):
        super().__init__(name)
        self.alarm = alarm