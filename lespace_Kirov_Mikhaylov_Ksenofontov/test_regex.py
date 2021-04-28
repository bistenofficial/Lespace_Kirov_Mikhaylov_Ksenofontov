import unittest
import myform

list_mail_false = ["m@mailru", "mamail.ru", "mail@", "testcom"]
list_mail_true = ["m@mail.ru", "mailup@mail.ru", "mail@mail.ru.ru", "test@gmail.com"]

class Test_test_2(unittest.TestCase):
    def test_T_mail(self):
        for str in list_mail_false:
            self.assertFalse(myform.reg_check(str))
    def test_F_mail(self):
        for str in list_mail_true:
            self.assertTrue(myform.reg_check(str))


if __name__ == '__main__':
    unittest.main()
