def longestCommandPrefix(strs):
    prefix = strs[0]
    for i in strs[1:]:
        idx = 0
        while idx < len(prefix) and idx < len(i):
            print(idx)
            if i[idx] == prefix[idx]:
                idx += 1 
            else:
                if idx == 0:
                    print('""')
                    return

        prefix = i[:idx]
        idx = 0

    print('"%s"' % ''.join(prefix))
    return
            

strs = ["ab", "a"]

longestCommandPrefix(strs)

strs2 = ["dog","racecar","car"]
longestCommandPrefix(strs2)
