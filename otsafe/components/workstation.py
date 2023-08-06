from components.generic import Component


class Workstation(Component):
    """
    This class is designed to represent an engineering, safety engineering, or other workstation. Includes default values for the host OS and application.  
    """

    def __init__(
        self,
        name: str,
        os: str = None,
        os_version: str = None,
        hostname: str = None,
        user: str = None,
        **kwargs
    ) -> None:
        
        super().__init__(name)
        self.os = os
        self.os_version = os_version
        self.hostname = hostname
        self.user = user
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)
