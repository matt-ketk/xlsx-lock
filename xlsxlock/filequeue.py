import re
from pathlib import Path

class FileQueue:
    def __init__(self):
        self.queue = []

    @staticmethod
    def filter_file(file_path):
        """Return True if file_path is a .xlsx or .xlsm file

        :file_path: (str) file path detected by watchdog 
        :returns: (bool) if file is .xlsx or .xlsm
        """
        return bool(re.search(r'\.xls[mx]$', file_path))

    def add_file(self, file_path):
        """Add the file in the queue to be operated on if it meets
        the requirements.

        :file_path: (str) file path passed in by watchdog
        :returns: (bool) True if successful

        """
        if FileQueue.filter_file(file_path):
            self.queue.append(file_path)
            return True
        else:
            return False

    def pop_file(self):
        """Return the next file path in the queue.

        :returns: (str) the file path popped off of the queue.

        """
        return self.queue.pop(0)

    def empty(self):
        """Return True if the queue is empty
        :returns: (bool) True if empty

        """
        return len(self.queue) == 0

