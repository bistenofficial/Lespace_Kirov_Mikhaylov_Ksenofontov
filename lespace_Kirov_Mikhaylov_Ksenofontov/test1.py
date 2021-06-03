import unittest
import re
import checks

class Test_data_test_correct(unittest.TestCase):
    def test_A(self):
        for i in checks.list_data_cor:
            self.assertTrue((checks.written_date_correct(i) is not None))
if __name__ == '__main__':
    unittest.main()
