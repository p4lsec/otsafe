import unittest
from otsafe.components.safety_systems import SIS
from otsafe.components.sensors import Sensor
from otsafe.components.actuators import Actuator

class TestSIS(unittest.TestCase):

    def setUp(self):
        sensor = Sensor(name="TestSensor")
        actuator = Actuator(name="TestActuator")
        self.sis = SIS(sensor=sensor, actuator=actuator)

    def test_initialization(self):
        self.assertIsInstance(self.sis.sensor, Sensor)
        self.assertIsInstance(self.sis.actuator, Actuator)

if __name__ == '__main__':
    unittest.main()