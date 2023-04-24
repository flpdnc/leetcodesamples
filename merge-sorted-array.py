def merge(nums1, m, nums2, n):
    """
    Merge sort without using 'sort'.
    """
    if m == 0:
        return nums2
    if n == 0:
        return nums1

    # If both lists have a length, then start merging into nums1
    # m is length is length of nums1 before adding nums2 length
    m_idx = 0
    n_idx = 0
    scratch = []
    while m_idx < m and n_idx < n:
        if nums1[m_idx] <= nums2[n_idx]:
            scratch.append(nums1[m_idx])
            m_idx += 1
        else:
            #nums1 = nums1[:m_idx] + [nums2[n_idx]] + nums1[m_idx:]
            scratch.append(nums2[n_idx])
            n_idx += 1

    # If either length is 0, nothing to do so just return sorted list
    if n_idx == n:
        blegh = scratch + nums1[m_idx:]
        for i in range(m + n):
            nums1[i] = blegh[i]
        return nums1
    else:
        for i in range(len(scratch)):
            nums1[i] = scratch[i]
        for i in range(n - n_idx):
            nums1[len(scratch) + i] = nums2[n_idx + i]
        return nums1




import unittest

class TestSqrtx(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])

    def test_second_sample(self):
        self.assertEqual(merge([1], 1, [], 0), [1])

    def test_third_sample(self):
        self.assertEqual(merge([0], 0, [1], 1), [1])

    def test_third_sample(self):
        self.assertEqual(merge([2, 0], 1, [1], 1), [1, 2])


if __name__ == '__main__':
    unittest.main()
