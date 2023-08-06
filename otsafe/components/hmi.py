from components.generic import Component


class HMI(Component):

    """
    This class is designed to represent a human machine interface (HMI).
    """

    def __init__(
        self, name: str, **kwargs
    ) -> None:
        
        super().__init__(name)
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)
