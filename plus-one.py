def plusOne(digits):
    if digits[-1] == 9 and len(digits) == 1:
        return [1] + [0]
    elif digits[-1] == 9:
        return plusOne(digits[:-1]) + [0]
    dig = digits[-1]
    return digits[:-1] +[dig + 1]






import unittest

class TestPlusOne(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(plusOne([1,2,3]), [1,2,4])

    def test_second_sample(self):
        self.assertEqual(plusOne([4,3,2,1]), [4,3,2,2])

    def test_third_sample(self):
        self.assertEqual(plusOne([9]), [1,0])

if __name__ == '__main__':
    unittest.main()
