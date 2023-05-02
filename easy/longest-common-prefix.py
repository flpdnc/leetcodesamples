def longestCommonPrefix(strs):
    def is_common_prefix(strs, length):
        prefix = strs[0][:length]
        return all(s.startswith(prefix) for s in strs)


    if not strs:
        return ""

    min_length = min(len(s) for s in strs)
    low, high = 1, min_length
    if is_common_prefix(strs, min_length):
        return strs[0][:min_length]
    while low <= high:
        mid = (low + high) // 2
        if is_common_prefix(strs, mid):
            low = mid + 1
        else:
            high = mid - 1

    return strs[0][:(low + high) // 2]

import unittest
            
class TestLongestCommonPrefix(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(longestCommonPrefix(["ab", "a"]), "a")

    def test_second_sample(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]), "")

    def test_third_sample(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")

if __name__ == '__main__':
    unittest.main()

