from otsafe.components.generic import Component


class Valve(Component):

    """
    This class is designed to represent a valve in the system.  It has a name, a state, and a percentage.

    The state can be used to represent a binary status of the valve.  The open_percentage is a float between 0.0 and 1.0, where 0.0 is 0% open (closed), and 1.0 is 100% open (fully open).

    """

    def __init__(
        self, name: str, state: bool = None, open_percentage: float = 0, **kwargs
    ) -> None:
        super().__init__(name)
        self.state = state
        self.open_percentage = open_percentage
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)
