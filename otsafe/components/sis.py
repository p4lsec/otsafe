from components.generic import Component


class SIS(Component):
    def __init__(self, name, state: bool = False, **kwargs):
        super().__init__(name)
        self.state = state
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)