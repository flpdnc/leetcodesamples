def strStr(haystack: str, needle: str) -> int:
    need_idx = 0
    hay_idx = 0
    max_hay_idx = len(haystack)
    needle_len = len(needle)
    while hay_idx < max_hay_idx:
        if haystack[hay_idx] == needle[need_idx]:
            # Check if this continues to end of need_len
            if need_idx + 1 == needle_len:
                return hay_idx - needle_len + 1
            else:
                hay_idx += 1
                need_idx += 1
        else:
            # Otherwise increment hay_idx back to start of needle_len and reset need_idx to 0
            hay_idx = hay_idx - need_idx + 1
            need_idx = 0
    return -1



# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

res = strStr('sadbutsad', 'sad')
print(res)

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1

res = strStr('leetcode', 'leeto')
print(res)

res = strStr('leetcode', 'e')
print(res)


res = strStr('mississippi', 'issip')
print(res)
