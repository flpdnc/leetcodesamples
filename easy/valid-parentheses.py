def isValid(s):
    open_order = list()

    for i in s:
        if i in ['(','{','[']:
            open_order.append(i)
        elif i in [')', '}', ']']:
            if len(open_order) == 0:
                return False
            match i:
                case ')':
                    if open_order.pop() != '(':
                        return False
                case '}':
                    if open_order.pop() != '{':
                        return False
                case ']':
                    if open_order.pop() != '[':
                        return False
    if open_order:
        return False
    else:
        return True
                    
import unittest

class TestIsValid(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(isValid("()"), True)

    def test_second_sample(self):
        self.assertEqual(isValid("()[]{}"), True)

    def test_third_sample(self):
        self.assertEqual(isValid("(]"), False)

if __name__ == '__main__':
    unittest.main()
