def isPalindrome(x):
    # Negative numbers return false because the - sign
    if x < 0:
        print("%s is not a palindrome" % x)
        return False
    # Single digits by default are palindromes
    if x < 10:
        print("%s is a palindrome" % x)
        return True

    # Condensed version without keeping track of each decimal place
    orig_x = x
    rev_x = 0

    while x != 0:
        # Get last digit from the right
        rem = x % 10
        # Shift over left one digit, and add last digit to the end
        rev_x = (rev_x * 10) + rem
        # drop last digit
        x = x // 10

    print(rev_x, orig_x)

    if rev_x == orig_x:
        return True
    return False
    





    # LONG WAY to figure out:
    """
    # Constraint is that it is less than 2^31 -1, so max 10 places to figure out.
    # Extra challenge of not converting to string first, so breaking number down
    # to work with it
    new_x = []
    digi_place = 1000000000
    while digi_place > 1:
        digi_app = x // digi_place
        print(digi_place, digi_app, new_x, x)
        if digi_app > 0 or len(new_x) > 0:
            new_x = [digi_app] + new_x
            x -= digi_place * digi_app
        digi_place = digi_place // 10
    new_x = [x] + new_x

    # Assemble back into a single int
    rev_x = 0
    digi_place = 1
    print(new_x)
    while len(new_x) > 0:
        digi = new_x.pop()
        rev_x += digi * digi_place
        digi_place *= 10

    # Now check if they are the same by dividing the original by the revsered, which should equal 1.
    print("%s and %s are the results" % (orig_x, rev_x))
    if rev_x == orig_x:
        print("%s is a palindrome" % orig_x)
        return True

    print("%s is not a palindrome" % orig_x)
    return False
    """


x = 121
isPalindrome(x)

x = -121
isPalindrome(x)

x = 10
isPalindrome(x)

x = 1001
isPalindrome(x)
