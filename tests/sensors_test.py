import unittest
from otsafe.components.sensors import Sensor

class TestSensor(unittest.TestCase):

    def setUp(self):
        self.sensor = Sensor(name="TestSensor")

    def test_initialization(self):
        self.assertEqual(self.sensor.id, "TestSensor")
        self.assertIsNone(self.sensor.value)
        self.assertEqual(self.sensor.unit, "")

if __name__ == '__main__':
    unittest.main()