def climbStairs(n):
    """
    Step size can only be 1 or two
    Find how many distinct ways to climb to top of the stairs
    """
    # It's a fibb sequence. The number of 'ways' up the stairs
    # will be combined of the previous two since you're adding
    # one more additional 'position' option.
    ways_prev = 1
    ways_new = 1
    holder = 0
    step_ways = 1
    i = 1
    while i < n:
        step_ways = ways_prev + ways_new
        holder = ways_new
        ways_new += ways_prev
        ways_prev = holder
        i += 1
    return step_ways









import unittest

class TestSqrtx(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(climbStairs(2), 2)

    def test_second_sample(self):
        self.assertEqual(climbStairs(3), 3)

    def test_third_sample(self):
        self.assertEqual(climbStairs(4), 5)

    def test_fourth_sample(self):
        self.assertEqual(climbStairs(1), 1)

    def test_fifth_sample(self):
        self.assertEqual(climbStairs(5), 8)


if __name__ == '__main__':
    unittest.main()
