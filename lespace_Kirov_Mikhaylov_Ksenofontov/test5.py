import unittest
import re
import checks

class Test_test_phone_cor(unittest.TestCase):
    def test_A(self):
        for i in checks.list_phone_сor:
            self.assertTrue((checks.author_phone(i) is not None))
if __name__ == '__main__':