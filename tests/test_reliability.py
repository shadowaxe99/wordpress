import unittest
from src import reliability

class TestReliability(unittest.TestCase):

    def setUp(self):
        self.reliability = reliability.ensure_reliability()

    def test_error_handling(self):
        self.assertIsNotNone(self.reliability.error_handling)
        self.assertTrue(callable(self.reliability.error_handling))

    def test_reporting_mechanism(self):
        self.assertIsNotNone(self.reliability.reporting_mechanism)
        self.assertTrue(callable(self.reliability.reporting_mechanism))

    def test_uninterrupted_service(self):
        self.assertIsNotNone(self.reliability.uninterrupted_service)
        self.assertTrue(callable(self.reliability.uninterrupted_service))

if __name__ == '__main__':
    unittest.main()