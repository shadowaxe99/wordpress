```python
import unittest
from src import performance

class TestPerformance(unittest.TestCase):

    def setUp(self):
        self.performance = performance.handle_performance()

    def test_handle_performance(self):
        self.assertEqual(self.performance, "Performance handled")

    def test_response_time(self):
        response_time = self.performance.get_response_time()
        self.assertTrue(response_time <= 2000, "Response time is within acceptable range")

    def test_content_curation_efficiency(self):
        efficiency = self.performance.get_content_curation_efficiency()
        self.assertTrue(efficiency >= 0.8, "Content curation is efficient")

if __name__ == '__main__':
    unittest.main()
```