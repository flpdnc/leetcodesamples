def longestPalindrome(s):
    longest = s[0]
    idx = 1 
    if len(set(s)) == 1:
        return s

    # Check if even or odd
    s_len = len(s)
    if s_len % 2 == 0:
        odd = False
    else:
        odd = True

    while idx < s_len:
        # Create holders for either side of pointer
        even_for_stack = []
        odd_for_stack = []
        for_stack = []
        rev_stack = []
        offset = 1
        candidate = ''

        while offset <= idx and idx + offset <= s_len:
            rev_stack.append(s[idx-offset])
            # Odd forward stack check, idx is the 'center'
            if idx + offset == s_len: 
                # Don't check odd case so we don't exceed length
                pass
            else:
                odd_for_stack.append(s[idx+offset])
            # Even forward stack check, idx is not the 'center'
            even_for_stack.append(s[idx+offset-1])
            # Check if both sides of pointer are mirror, odd number
            if rev_stack == odd_for_stack:
                candidate = s[idx-offset:idx+offset+1]
                offset += 1
            # Check if it's an even number, so for stack shaved one
            elif rev_stack == even_for_stack:
                candidate = s[idx-offset:idx+offset]
                offset += 1
            else:
                offset = idx + 1
                rev_stack = []
                odd_for_stack = []
                even_for_stack = []
                candidate = ''
                
            if len(candidate) > len(longest):
                longest = candidate

        idx += 1
    return longest





import unittest

class TestSqrtx(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(longestPalindrome('babad'), 'bab')
    def test_second_sample(self):
        self.assertEqual(longestPalindrome('bbbbbb'), 'bbbbbb')
    def test_third_sample(self):
        self.assertEqual(longestPalindrome('cbbd'), 'bb')
    def test_fourth_sample(self):
        self.assertEqual(longestPalindrome('ac'), 'a')
    def test_fifth_sample(self):
        self.assertEqual(longestPalindrome('abb'), 'bb')
    def test_sixth_sample(self):
        self.assertEqual(longestPalindrome('tattarrattat'), 'tattarrattat')


if __name__ == '__main__':
    unittest.main()
