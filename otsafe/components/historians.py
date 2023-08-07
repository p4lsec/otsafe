from otsafe.components.generic import Component


class Historian(Component):

    """
    This class is designed to represent a Historian server. 
    """

    def __init__(
        self,
        name: str,
        os: str = None,
        os_version: str = None,
        hostname: str = None,
        user: str = None,
        application_name: str = None,
        application_version: str = None,
        **kwargs
    ) -> None:
        
        super().__init__(name)
        self.os = os
        self.os_version = os_version
        self.hostname = hostname
        self.user = user
        self.application_name = application_name
        self.application_version = application_version
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)
