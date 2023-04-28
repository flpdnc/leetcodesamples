def lengthOfLongestSubstring(s):
    letter_stack = []
    longest = 0
    idx = 0
    while idx < len(s):
        next_letter = s[idx]
        if next_letter in letter_stack:
            idx = (idx - len(letter_stack)) + 1
            letter_stack = []
        else:
            letter_stack.append(s[idx])
            idx += 1
            longest = max(longest, len(letter_stack))
    return longest





import unittest

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(lengthOfLongestSubstring('abcabcbb'), 3)
    def test_second_sample(self):
        self.assertEqual(lengthOfLongestSubstring('bbbbbb'), 1)
    def test_third_sample(self):
        self.assertEqual(lengthOfLongestSubstring('pwwkew'), 3)

if __name__ == '__main__':
    unittest.main()
