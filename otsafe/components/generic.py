from pymodbus.client import ModbusTcpClient
from datetime import datetime
from uuid import uuid4

class Component:
    def __init__(
        self,
        id: str,
        ip: str = None,
        port: int = None,
        description: str = None,
        **kwargs
    ):

        self.id = id or str(uuid4())
        self.ip = ip
        self.port = port
        self.description = description
        self.created_at = datetime.now()
        
        # Apply kwargs last so they can override the defaults
        self.__dict__.update(kwargs)

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id

    def __ne__(self, other):
        return self.id != other.id

    def __hash__(self):
        return hash(self.id)

    def read_modbus(self, register, count):
        client = ModbusTcpClient(self.ip, self.port)
        client.connect()
        result = client.read_holding_registers(register, count)
        client.close()
        return result

    def write_modbus(self, register, value):
        client = ModbusTcpClient(self.ip, self.port)
        client.connect()
        result = client.write_register(register, value)
        client.close()
        return result
