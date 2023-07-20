from components.generic import Component


class Pump(Component):
    def __init__(self, name, state: bool = False, rpm: int = 0):
        super().__init__(name)
        self.state = state
        self.rpm = rpm