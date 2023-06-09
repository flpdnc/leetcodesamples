def removeElement(nums, val):
    k = len(nums)
    i = 0
    while i < len(nums):
        if nums[i] == val:
            # Don't increment i since we just removed it.
            k -= 1
            del nums[i]
        else:
            i += 1
    return (k, nums)






import unittest

class TestPlusOne(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(removeElement([3,2,2,3], 3), (2, [2,2]))

    def test_second_sample(self):
        self.assertEqual(removeElement([0,1,2,2,3,0,4,2], 2), (5, [0,1,3,0,4]))

    def test_third_sample(self):
        pass

if __name__ == '__main__':
    unittest.main()
