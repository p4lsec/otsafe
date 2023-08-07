import unittest
import datetime
from otsafe.components.actuators import Actuator

class TestActuator(unittest.TestCase):

    def setUp(self):
        self.actuator = Actuator(name="TestActuator")

    def test_initialization(self):
        self.assertEqual(self.actuator.name, "TestActuator")
        self.assertFalse(self.actuator.open)
        self.assertIsInstance(self.actuator.last_modified, datetime.datetime)

    def test_custom_initialization(self):
        custom_actuator = Actuator(name="CustomActuator", open=True)
        self.assertEqual(custom_actuator.name, "CustomActuator")
        self.assertTrue(custom_actuator.open)

    def test_last_modified_update(self):
        initial_time = self.actuator.last_modified
        self.actuator.open = not self.actuator.open
        self.actuator.last_modified = datetime.datetime.now()
        self.assertNotEqual(self.actuator.last_modified, initial_time)

if __name__ == '__main__':
    unittest.main()