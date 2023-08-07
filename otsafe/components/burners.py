from otsafe.components.generic import Component


class Burner(Component):
    def __init__(self, name: str, flame: bool = True, temperature: int = 0, **kwargs):
        super().__init__(name)
        self.name = name
        self.flame = flame
        self.temperature = temperature
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)
