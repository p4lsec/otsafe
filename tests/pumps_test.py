import unittest
from otsafe.components.pumps import Pump

class TestPump(unittest.TestCase):

    def setUp(self):
        self.pump = Pump(name="TestPump")

    def test_initialization(self):
        self.assertEqual(self.pump.id, "TestPump")
        self.assertFalse(self.pump.state)
        self.assertEqual(self.pump.rpm, 0)

    def test_custom_initialization(self):
        custom_pump = Pump(name="CustomPump", state=True, rpm=1500)
        self.assertEqual(custom_pump.id, "CustomPump")
        self.assertTrue(custom_pump.state)
        self.assertEqual(custom_pump.rpm, 1500)

    def test_rpm_update(self):
        self.pump.rpm = 2000
        self.assertEqual(self.pump.rpm, 2000)

if __name__ == '__main__':
    unittest.main()
