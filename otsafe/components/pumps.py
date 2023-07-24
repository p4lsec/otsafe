from components.generic import Component


class Pump(Component):
    def __init__(self, name, state: bool = False, rpm: int = 0, **kwargs):
        super().__init__(name)
        self.state = state
        self.rpm = rpm
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)