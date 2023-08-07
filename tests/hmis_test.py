import unittest
from otsafe.components.hmis import HMI

class TestHMI(unittest.TestCase):

    def setUp(self):
        self.hmi = HMI(name="TestHMI")

    def test_initialization(self):
        self.assertEqual(self.hmi.id, "TestHMI")

if __name__ == '__main__':
    unittest.main()