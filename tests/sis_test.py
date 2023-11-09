import unittest
from unittest.mock import patch, MagicMock
from otsafe.components.sis import SIS  # Import the SIS class from the module where it's defined.

class TestSIS(unittest.TestCase):

    def setUp(self):
        self.sis = SIS(name="Pressure Sensor", value=100, unit="kPa")

    def test_initialization(self):
        self.assertEqual(self.sis.name, "Pressure Sensor")
        self.assertEqual(self.sis.value, 100)
        self.assertEqual(self.sis.unit, "kPa")

    @patch('otsafe.components.sis.SIS.raise_alarm')
    def test_set_min_alarm(self, mock_raise_alarm):
        self.sis.set_min_alarm(90)
        self.assertEqual(self.sis.min_alarm_value, 90)

    @patch('otsafe.components.sis.SIS.raise_alarm')
    def test_set_max_alarm(self, mock_raise_alarm):
        self.sis.set_max_alarm(110)
        self.assertEqual(self.sis.max_alarm_value, 110)

    def test_raise_alarm(self):
        with patch('otsafe.components.sis.Alarm') as mock_alarm:
            alarm = self.sis.raise_alarm("Test alarm")
            mock_alarm.assert_called_once_with(alarm=True, name=self.sis.name, message="Test alarm")

    def test_read(self):
        self.assertEqual(self.sis.read(), "100kPa")

    @patch('otsafe.components.sis.SIS.raise_alarm')
    def test_run_check(self, mock_raise_alarm):
        # Set up initial conditions
        self.sis.min_alarm_value = 50
        self.sis.max_alarm_value = 150

        # Case where value is below min_alarm_value
        self.sis.value = 40
        # self.sis.run(check=True)
        # mock_raise_alarm.assert_called_once_with("Min alarm SIS triggered!")

        # Case where value is above max_alarm_value
        self.sis.value = 160
        # self.sis.run(check=True)
        # mock_raise_alarm.assert_called_once_with("Max alarm SIS triggered!")

        # Case where value is between min and max alarm values
        self.sis.value = 100
        status = self.sis.run(check=True)
        # mock_raise_alarm.assert_not_called()
        self.assertEqual(status, "SIS operating nominally.")

if __name__ == '__main__':
    unittest.main()