from otsafe.components.generic import Component


class Controller(Component):
    """
    This class represents a controller.  This could be a PLC, DCS, or other digital device that can execute logic and send commands. s
    """

    def __init__(self, name, state: bool = False, **kwargs):
        super().__init__(name)
        self.name = name
        self.state = state
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)