def sqrtx(x):
    potential_res = 1
    sqr_res = 1
    if x < 2:
        return x
    while sqr_res <= x:
        potential_res += 1
        sqr_res = potential_res * potential_res
    return potential_res - 1









import unittest

class TestSqrtx(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(sqrtx(4), 2)

    def test_second_sample(self):
        self.assertEqual(sqrtx(8), 2)

    def test_third_sample(self):
        self.assertEqual(sqrtx(16), 4)

    def test_fourth_sample(self):
        self.assertEqual(sqrtx(27), 5)

    def test_fifth_sample(self):
        self.assertEqual(sqrtx(2), 1)


if __name__ == '__main__':
    unittest.main()
