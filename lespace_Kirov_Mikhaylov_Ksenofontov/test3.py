import unittest
import re
import checks

class Test_test_3(unittest.TestCase):
    def test_A(self):
        for i in checks.list_mail_cor:
            self.assertTrue((checks.author_email_correct(i) is not None))
if __name__ == '__main__':
    unittest.main()
