class UnsafeCondition(Exception):
    """Raised when an unsafe conidition is detected"""
    def __init__(self, message="An unsafe condition detected"):
        self.message = message
        super().__init__(self.message)

class ConnectionError(Exception):
    """Raised when a connection error occurs"""
    def __init__(self, message="Unable to connect"):
        self.message = message
        super().__init__(self.message)

class ImpossibleCondition(Exception):
    """Raised when an impossible situation was detected (example: burner on max but no heat detected)"""
    def __init__(self, message="Invalid condition detected"):
        self.message = message
        super().__init__(self.message)

class ComponentNotAlive(Exception):
    """Raised when a component is not alive"""
    def __init__(self, message="Component is not alive"):
        self.message = message
        super().__init__(self.message)