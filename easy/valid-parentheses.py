def isValid(s):
    paren_open = 0
    open_order = []

    for i in s:
        print(i)
        if i in ['(','{','[']:
            open_order.append(i)
            paren_open += 1
        elif i in [')', '}', ']']:
            if len(open_order) == 0:
                return False
            match i:
                case ')':
                    if open_order[-1] != '(':
                        return False
                    else:
                        open_order = open_order[:-1]
                case '}':
                    if open_order[-1] != '{':
                        return False
                    else:
                        open_order = open_order[:-1]
                case ']':
                    if open_order[-1] != '[':
                        return False
                    else:
                        open_order = open_order[:-1]
    if open_order:
        return False
    else:
        return True
                    










s = "()"
s2 = "()[]{}"
s3 = "(]"
print(isValid(s))
print(isValid(s2))
print(isValid(s3))

