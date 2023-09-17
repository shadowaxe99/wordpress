```python
import multiprocessing
from src.utils import get_system_resources

def scale_system():
    """
    Function to scale the system horizontally to accommodate increased traffic and content volume.
    """
    # Get the current system resources
    current_resources = get_system_resources()

    # Check if the system resources are sufficient for the current load
    if current_resources['cpu_usage'] > 80 or current_resources['memory_usage'] > 80:
        # If the system resources are not sufficient, scale up the system
        scale_up_system()
    elif current_resources['cpu_usage'] < 30 and current_resources['memory_usage'] < 30:
        # If the system resources are underutilized, scale down the system
        scale_down_system()

def scale_up_system():
    """
    Function to scale up the system by adding more resources.
    """
    # Get the number of available CPUs
    num_cpus = multiprocessing.cpu_count()

    # Double the number of CPUs
    num_cpus *= 2

    # Update the system resources
    update_system_resources(num_cpus=num_cpus)

def scale_down_system():
    """
    Function to scale down the system by reducing resources.
    """
    # Get the number of available CPUs
    num_cpus = multiprocessing.cpu_count()

    # Halve the number of CPUs
    num_cpus //= 2

    # Update the system resources
    update_system_resources(num_cpus=num_cpus)

def update_system_resources(num_cpus):
    """
    Function to update the system resources.
    """
    # Update the number of CPUs
    multiprocessing.set_start_method('forkserver', force=True)
    multiprocessing.cpu_count = num_cpus
```