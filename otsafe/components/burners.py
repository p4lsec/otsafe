from components.generic import Component


class Burner(Component):
    def __init__(self, name: str, flame: bool = True, temperature: int = 0):
        super().__init__(name)
        self.flame = flame
        self.temperature = temperature
