import unittest
import myform_mail

class Test_test_1(unittest.TestCase):
    def setUp(self):
        self.data = ["m.m@mail.ru","ml@gmail.com","somemail@domain.any.com"]
    def test_correct(self):
        for element in self.data:
            self.assertTrue(myform_mail.correct(element))
if __name__ == '__main__':
    unittest.main()

