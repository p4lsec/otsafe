import unittest
from otsafe.components.servers import Server

class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = Server(name="TestServer")

    def test_initialization(self):
        self.assertEqual(self.server.id, "TestServer")
        self.assertIsNone(self.server.os)
        self.assertIsNone(self.server.os_version)
        self.assertIsNone(self.server.hostname)
        self.assertIsNone(self.server.user)
        self.assertIsNone(self.server.application_name)
        self.assertIsNone(self.server.application_version)

    def test_custom_initialization(self):
        custom_server = Server(name="CustomServer", os="Linux", os_version="5.10", hostname="localhost", user="admin", application_name="App", application_version="1.0")
        self.assertEqual(custom_server.id, "CustomServer")
        self.assertEqual(custom_server.os, "Linux")
        self.assertEqual(custom_server.os_version, "5.10")
        self.assertEqual(custom_server.hostname, "localhost")
        self.assertEqual(custom_server.user, "admin")
        self.assertEqual(custom_server.application_name, "App")
        self.assertEqual(custom_server.application_version, "1.0")

if __name__ == '__main__':
    unittest.main()
