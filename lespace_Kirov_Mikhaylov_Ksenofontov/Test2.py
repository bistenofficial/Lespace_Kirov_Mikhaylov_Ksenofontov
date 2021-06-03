import unittest
import re
import checks

class Test_data_test_incorrect(unittest.TestCase):
    def test_A(self):
        for i in checks.list_data_uncor:
            self.assertFalse((checks.written_date_correct(i)))
if __name__ == '__main__':
    unittest.main()
