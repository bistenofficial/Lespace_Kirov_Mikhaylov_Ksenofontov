import unittest
import Check

class Test_test_4(unittest.TestCase):
    def test_uncorrect(self):
        data1 = ["832 (7654) 423234+324+324","LKJHGFD","8(932)777-43-324","8 (53432) 234-23-23", "8 (434) 7654-43-34","8 (912) 432-34-34-34","8 323 323-23-32"]
        for str in data1:
            self.assertFalse(Check.check_phone(str))
if __name__ == '__main__':
    unittest.main()
