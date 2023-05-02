
def twoSum(nums, target):
    can_sum = False

    sum_check = {}
    for i,num in enumerate(nums):
        if num in sum_check:
            return [sum_check[num], i]
            #print([sum_check[num], i])
            #return
        target_match = target - num
        sum_check[target_match] = i


import unittest

class TestTwoSum(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(twoSum([3,3], 6), [0,1])

    def test_second_sample(self):
        self.assertEqual(twoSum([3,2,4], 6), [1,2])

    def test_third_sample(self):
        self.assertEqual(twoSum([2,7,11,15], 9), [0,1])

if __name__ == '__main__':
    unittest.main()
