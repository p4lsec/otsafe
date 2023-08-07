import unittest
from otsafe.components.workstations import Workstation

class TestWorkstation(unittest.TestCase):

    def setUp(self):
        self.workstation = Workstation(name="TestWorkstation")

    def test_initialization(self):
        self.assertEqual(self.workstation.id, "TestWorkstation")
        self.assertIsNone(self.workstation.os)
        self.assertIsNone(self.workstation.os_version)
        self.assertIsNone(self.workstation.hostname)
        self.assertIsNone(self.workstation.user)

if __name__ == '__main__':
    unittest.main()