import unittest
import re
import checks

class Test_data_test_correct(unittest.TestCase):
    def test_A(self):
        for i in checks.list_data_cor:
            self.assertTrue((checks.written_date_correct(i) is not None))
if __name__ == '__main__':
    unittest.main()

class Test_data_test_incorrect(unittest.TestCase):
    def test_A(self):
        for i in checks.list_data_uncor:
            self.assertFalse((checks.written_date_correct(i)))
if __name__ == '__main__':
    unittest.main()

class Test_test_3(unittest.TestCase):
    def test_A(self):
        for i in checks.list_mail_cor:
            self.assertTrue((checks.author_email_correct(i) is not None))
if __name__ == '__main__':
    unittest.main()

class AssertFalseTest(unittest.TestCase):
    def test_A(self):
        for j in checks.list_mail_uncor:
            self.assertFalse((checks.author_email_correct(j)))
if __name__ == '__main__':
    unittest.main()

class Test_test_phone_cor(unittest.TestCase):
    def test_A(self):
        for i in checks.list_phone_сor:
            self.assertTrue((checks.author_phone(i) is not None))
if __name__ == '__main__':
    unittest.main()

class Test_test_phone_cor(unittest.TestCase):
    def test_A(self):
        for i in checks.list_phone_uncor:
            self.assertFalse(checks.author_phone(i))
if __name__ == '__main__':
    unittest.main()
