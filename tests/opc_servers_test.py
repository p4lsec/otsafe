import unittest
from otsafe.components.opc_servers import OPCServer

class TestOPCServer(unittest.TestCase):

    def setUp(self):
        self.opc = OPCServer(name="TestOPC")

    def test_initialization(self):
        self.assertEqual(self.opc.id, "TestOPC")
        self.assertIsNone(self.opc.os)
        self.assertIsNone(self.opc.os_version)
        self.assertIsNone(self.opc.hostname)
        self.assertIsNone(self.opc.user)

if __name__ == '__main__':
    unittest.main()