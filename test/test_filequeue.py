import unittest
from xlsxlock import filequeue

class TestFileQueue(unittest.TestCase):

    """Test Queueing functionality as xlsx/m files enter the directory."""
    
    def setUp(self):
        """Set up a test FileQueue

        """
        self.directory_paths = ['2010-10-08-report.xlsx', '2020-07-09-report.xlsm',
            'abcdef.txt', 'spam.csv', 'abcdef.xlsx', 'spam.xlsm', 'thisisadir/']
        self.correct_paths = [True, True, False, False, True, True, False]
        self.test_queue = filequeue.FileQueue()
        
    def test_filter_file(self):
        """Tests selection of the correct file extensions (.xlsx, .xlsm)

        """

        for i in range(len(self.directory_paths)):
            self.assertEqual(filequeue.FileQueue.filter_file(self.directory_paths[i]),
                self.correct_paths[i])

    def test_add_file(self):
        """Tests adding of the correct files to the queue

        """
        for i in range(len(self.directory_paths)):
            self.assertEqual(self.test_queue.add_file(self.directory_paths[i]),
                    self.correct_paths[i])

    def test_empty(self):
        """Test the empty check functionality
        :returns: TODO

        """
        self.assertTrue(self.test_queue.empty())
        for path in self.directory_paths:
            self.test_queue.add_file(path)
            self.assertFalse(self.test_queue.empty())

    def test_pop_file(self):
        filtered_paths = []
        for i in range(len(self.directory_paths)):
            if self.correct_paths[i]:
                filtered_paths.append(self.directory_paths[i])

        for path in self.directory_paths:
            self.test_queue.add_file(path)

        while not self.test_queue.empty():
            self.assertIn(self.test_queue.pop_file(), filtered_paths)

        # when it is empty, test one more time
        with self.assertRaises(IndexError):
            self.test_queue.pop_file()

        
        
