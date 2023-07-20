from components.generic import Component


class Vessel(Component):
    def __init__(self, name: str, volume: int = 0):
        super().__init__(name)
        self.volume = volume