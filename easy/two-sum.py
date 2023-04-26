#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#Example 3:
#
#Input: nums = [3,3], target = 6
#Output: [0,1]


def twoSum(nums, target):
    can_sum = False

    sum_check = {}
    for i,num in enumerate(nums):
        if num in sum_check:
            print([sum_check[num], i])
            return
        target_match = target - num
        sum_check[target_match] = i

twoSum([3,3], 6)
twoSum([3,2,4], 6)
twoSum([2,7,11,15], 9)
