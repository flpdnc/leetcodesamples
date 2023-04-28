def myAtoi(s):
    s_len = len(s)
    neg = False
    pos = False
    s_int = []
    int_end = False
    i = 0

    for i in s:
        # Skip leading white space
        if i == " " and len(s_int) == 0 and not pos and not neg:
            continue
        elif i == '-' and len(s_int) == 0 and not neg:
            neg = True
        elif i == '+' and len(s_int) == 0 and not pos:
            pos = True
        elif pos == True and neg == True:
            return 0 
        elif i.isdigit():
            s_int.append(i)
        else:
            break
    
    
    x = 0
    digi_place = 1
    while len(s_int) > 0:
        x += int(s_int.pop()) * digi_place
        digi_place *= 10

    if neg:
        x = x * -1
        if x < -2 ** 31:
            return 0
        else:
            return x
    else:
        if x > (2 ** 31) - 1:
            return 0
        else:
            return x



import unittest

class TestmyAtoi(unittest.TestCase):

    def test_first_sample(self):
        self.assertEqual(myAtoi("123"), 123)

    def test_second_sample(self):
        self.assertEqual(myAtoi("42"), 42)

    def test_third_sample(self):
        self.assertEqual(myAtoi("   -42"), -42)

    def test_fourth_sample(self):
        self.assertEqual(myAtoi("4193 with words"), 4193)

if __name__ == '__main__':
    unittest.main()
