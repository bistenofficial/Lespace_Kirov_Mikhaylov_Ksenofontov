import unittest, re, checks

class AssertFalseTest(unittest.TestCase):
    def test_A(self):
        for j in checks.list_mail_uncor:
            self.assertFalse((checks.author_email_correct(j)))
if __name__ == '__main__':
    unittest.main()

