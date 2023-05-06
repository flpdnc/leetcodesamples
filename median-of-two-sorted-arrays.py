def findMedianSortedArrays(nums1, nums2):
    merged = []
    idx1 = 0
    idx2 = 0
    m = len(nums1)
    n = len(nums2)
    # Merge sorted arrays
    while idx1 < m and idx2 < n:
        if nums1[idx1] <= nums2[idx2]:
            merged.append(nums1[idx1])
            idx1 += 1
        else:
            merged.append(nums2[idx2])
            idx2 += 1
    if idx1 < m:
        merged = merged + nums1[idx1:]
    else:
        merged = merged + nums2[idx2:]

    # Find middle of merged, if m + n is odd, then there's a middle.
    # If m + n is even, then average the two.
    t_len = m + n
    if t_len % 2:
        mid = t_len // 2
        return float(merged[mid])
    else:
        mid = t_len // 2
        return float((merged[mid] + merged[mid-1]) / 2.0)
        
# Constraints
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

import unittest

class TestFindMedianSortedArrays(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(findMedianSortedArrays([1,3], [2]), 2.0)

    def test_second_sample(self):
        self.assertEqual(findMedianSortedArrays([1,2], [3,4]), 2.5)


if __name__ == '__main__':
    unittest.main()

