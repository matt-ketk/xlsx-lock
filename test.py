import unittest
from config import directories

from pathlib import Path

class TestDirectory(unittest.TestCase):
    def test_no_dir(self):
        """ Test if one of the directories does not exist. """
        pass




class TestFileWatch(unittest.TestCase):
    """ Test if the file watcher picks the right files """
    def test_bad_extension(self):
        pass



class TestFileOpen(unittest.TestCase):
    pass

class TestXlsxLock(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()


