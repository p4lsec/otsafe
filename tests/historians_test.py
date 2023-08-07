import unittest
from otsafe.components.historians import Historian

class TestHistorian(unittest.TestCase):

    def setUp(self):
        self.historian = Historian(name="TestHistorian")

    def test_initialization(self):
        self.assertEqual(self.historian.id, "TestHistorian")
        self.assertIsNone(self.historian.os)
        self.assertIsNone(self.historian.os_version)
        self.assertIsNone(self.historian.hostname)
        self.assertIsNone(self.historian.user)
        self.assertIsNone(self.historian.application_name)
        self.assertIsNone(self.historian.application_version)

if __name__ == '__main__':
    unittest.main()