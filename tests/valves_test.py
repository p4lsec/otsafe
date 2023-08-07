import unittest
from otsafe.components.valves import Valve

class TestValve(unittest.TestCase):

    def setUp(self):
        self.valve = Valve(name="TestValve")

    def test_initialization(self):
        self.assertEqual(self.valve.id, "TestValve")
        self.assertIsNone(self.valve.state)
        self.assertEqual(self.valve.open_percentage, 0)

if __name__ == '__main__':
    unittest.main()