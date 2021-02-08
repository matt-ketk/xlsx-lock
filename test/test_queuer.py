import unittest
from xlsxlock import queuer

class TestQueuer(unittest.TestCase):

    """Docstring for TestQueuer. """

    def test_filter_file(self):
        """TODO: Docstring for test_queue_filter.
        :returns: TODO

        """
        directory_paths = ['2010-10-08-report.xlsx', '2020-07-09-report.xlsm',
                'abcdef.txt', 'spam.csv', 'abcdef.xlsx', 'spam.xlsm', 'thisisadir/']
        correct_paths = [True, True, False, False, True, True, False]

        for i in range(len(directory_paths)):
            self.assertEqual(queuer.filter_file(directory_paths[i]),
                    correct_paths[i])

