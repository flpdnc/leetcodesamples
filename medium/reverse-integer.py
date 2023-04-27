def reverse(x):
    # Check if negative value, discard negative, and store sign to add later.
    if x == 0:
        return x
    elif x < 0:
        neg = True
        x = x * -1
    else:
        neg = False
    
    digits = []
    while x > 0:
        digits.append(x % 10)
        x = x // 10

    rev_x = 0
    digi_place = 1
    while len(digits) > 0:
        rev_x += digits.pop() * digi_place
        digi_place *= 10

    # Reapply negative sign and check if overflow
    if neg:
        rev_x = rev_x * -1
        if rev_x < -2 ** 31:
            return 0
        else:
            return rev_x
    else:
        if rev_x > (2 ** 31) - 1:
            return 0
        else:
            return rev_x




import unittest

class TestReverse(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(reverse(123), 321)

    def test_second_sample(self):
        self.assertEqual(reverse(-123), -321)

    def test_third_sample(self):
        self.assertEqual(reverse(120), 21)

    def test_fourth_sample(self):
        self.assertEqual(reverse(1534236469), 0)

    def test_fifth_sample(self):
        self.assertEqual(reverse(-2147483648), 0)

if __name__ == '__main__':
    unittest.main()
