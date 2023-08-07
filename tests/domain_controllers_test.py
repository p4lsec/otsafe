import unittest
from otsafe.components.domain_controllers import DomainController

class TestDomainController(unittest.TestCase):

    def setUp(self):
        self.dc = DomainController(
            name="TestDC",
            os="Windows Server 2019",
            os_version="10.0.17763",
            hostname="TestDC",
            user="NT AUTHORITY\\SYSTEM",
            application_name="TestApp",
            application_version="1.0.0"
        )

    def test_initialization(self):
        self.assertEqual(self.dc.id, "TestDC")
        self.assertEqual(self.dc.os, "Windows Server 2019")
        self.assertEqual(self.dc.os_version, "10.0.17763")
        self.assertEqual(self.dc.hostname, "TestDC")
        self.assertEqual(self.dc.user, "NT AUTHORITY\\SYSTEM")
        self.assertEqual(self.dc.application_name, "TestApp")
        self.assertEqual(self.dc.application_version, "1.0.0")

if __name__ == '__main__':
    unittest.main()