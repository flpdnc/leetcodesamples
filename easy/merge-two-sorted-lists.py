def mergeTwoLists(list1, list2):
    list1_len = len(list1)
    idx1 = 0
    list2_len = len(list2)
    idx2 = 0

    merged_list = []
    if list1_len == 0 and list2_len == 0:
        return merged_list
    while idx1 < list1_len or idx2 < list2_len:
        if idx1 < list1_len and idx2 < list2_len:
            if list1[idx1] < list2[idx2]:
                merged_list.append(list1[idx1])
                idx1 += 1
            else:
                merged_list.append(list2[idx2])
                idx2 += 1
        elif idx1 < list1_len and idx2 == list2_len:
            merged_list += list1[idx1:]
            idx1 = list1_len
        else:
            merged_list += list2[idx2:]
            idx2 = list2_len
    return merged_list







list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))

list1 = []
list2 = []
print(mergeTwoLists(list1, list2))

list1 = []
list2 = [0]
print(mergeTwoLists(list1, list2))
