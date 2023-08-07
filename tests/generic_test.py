import unittest
from otsafe.components.generic import Component

class TestComponent(unittest.TestCase):

    def setUp(self):
        self.component = Component(id="TestComponent")

    def test_initialization(self):
        self.assertEqual(self.component.id, "TestComponent")
        self.assertIsNone(self.component.ip)
        self.assertIsNone(self.component.port)
        self.assertIsNone(self.component.description)

    def test_str_representation(self):
        self.assertEqual(str(self.component), "TestComponent")

    def test_repr_representation(self):
        self.assertEqual(repr(self.component), "TestComponent")

if __name__ == '__main__':
    unittest.main()