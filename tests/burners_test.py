import unittest
from otsafe.components.burners import Burner

class TestBurner(unittest.TestCase):

    def setUp(self):
        self.burner = Burner(name="TestBurner")

    def test_initialization(self):
        self.assertEqual(self.burner.name, "TestBurner")
        self.assertTrue(self.burner.flame)
        self.assertEqual(self.burner.temperature, 0)

    def test_custom_initialization(self):
        custom_burner = Burner(name="CustomBurner", flame=False, temperature=100)
        self.assertEqual(custom_burner.name, "CustomBurner")
        self.assertFalse(custom_burner.flame)
        self.assertEqual(custom_burner.temperature, 100)

    def test_temperature_update(self):
        initial_temp = self.burner.temperature
        self.burner.temperature = 50
        self.assertNotEqual(self.burner.temperature, initial_temp)
        self.assertEqual(self.burner.temperature, 50)

if __name__ == '__main__':
    unittest.main()