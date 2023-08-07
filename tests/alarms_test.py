import unittest
from otsafe.components.alarms import Alarm

class TestAlarm(unittest.TestCase):

    def setUp(self):
        self.alarm = Alarm(name="TestAlarm")

    def test_initialization(self):
        self.assertFalse(self.alarm.alarm)
        self.assertIsNone(self.alarm.message)

    def test_message(self):
        self.alarm.message = "Test message"
        self.assertEqual(self.alarm.message, "Test message")

if __name__ == '__main__':
    unittest.main()