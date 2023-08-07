import unittest
from otsafe.components.controllers import Controller

class TestController(unittest.TestCase):

    def setUp(self):
        self.controller = Controller(name="TestController")

    def test_initialization(self):
        self.assertEqual(self.controller.id, "TestController")
        self.assertFalse(self.controller.state)

    def test_state_update(self):
        self.controller.state = True
        self.assertTrue(self.controller.state)

if __name__ == '__main__':
    unittest.main()