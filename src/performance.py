```python
import time
from src.utils import get_current_time

class Performance:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = get_current_time()

    def stop_timer(self):
        self.end_time = get_current_time()

    def get_execution_time(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        else:
            return None

    def handle_performance(self, function, *args):
        self.start_timer()
        result = function(*args)
        self.stop_timer()
        execution_time = self.get_execution_time()
        if execution_time > 1.0:  # If execution time is more than 1 second
            print(f"Warning: {function.__name__} took {execution_time} seconds to execute.")
        return result

performance = Performance()

def handle_performance(function):
    def wrapper(*args, **kwargs):
        performance.start_timer()
        result = function(*args, **kwargs)
        performance.stop_timer()
        execution_time = performance.get_execution_time()
        if execution_time > 1.0:  # If execution time is more than 1 second
            print(f"Warning: {function.__name__} took {execution_time} seconds to execute.")
        return result
    return wrapper
```