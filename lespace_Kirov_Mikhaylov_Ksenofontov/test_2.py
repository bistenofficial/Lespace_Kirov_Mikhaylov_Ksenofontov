import unittest
import myform_mail

class Test_test_2(unittest.TestCase):
    def setUp(self):
        self.data = ["","1","m1@","@mail","gmail@some","@@mail.ru"]
    def test_uncorrect(self):
        for i in self.data:
            self.assertFalse(myform_mail.uncorrect(i))
if __name__ == '__main__':
    unittest.main()
