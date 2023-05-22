import os
import sys

# path to this file's directory and parent directory
file_path = os.path.abspath(__file__)
base_directory = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))

# add to path
sys.path.append(base_directory)

# define paths to each app dockerfile location
processor_path = os.path.join(base_directory, 'quick_batch', 'processor_app')
queue_path = os.path.join(base_directory, 'quick_batch', 'queue_app')




print(f"processor_path: {processor_path}")
print(f"queue_path: {queue_path}")
