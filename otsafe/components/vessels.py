from otsafe.components.generic import Component


class Vessel(Component):
    def __init__(self, name: str, volume: int = 0, **kwargs):
        super().__init__(name)
        self.volume = volume
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)