import unittest
import Check
#Тест для проверки регулярного выражения
class Test_test_3(unittest.TestCase):
    def test_correct(self):
        data = ["8 (932) 999-00-32","+7 (000) 000-00-00", "8 (999) 999-99-99","+7 (921) 777-63-63","8 (963) 882-52-29"]
        for str in data:
            self.assertTrue(Check.check_phone(str))
if __name__ == '__main__':
    unittest.main()
