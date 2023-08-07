import unittest
from otsafe.components.vessels import Vessel

class TestVessel(unittest.TestCase):

    def setUp(self):
        self.vessel = Vessel(name="TestVessel")

    def test_initialization(self):
        self.assertEqual(self.vessel.id, "TestVessel")
        self.assertEqual(self.vessel.volume, 0)

if __name__ == '__main__':
    unittest.main()