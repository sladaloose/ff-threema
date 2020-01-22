import unittest
import threemaScript

class TestThreemaScript(unittest.TestCase):

    def test_helloWorld(self):
        value = threemaScript.helloWorld("Hello World")
        self.assertEqual(value, 'Hello World')



if __name__ == '__main__':
    unittest.main()