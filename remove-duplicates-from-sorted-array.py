def removeDuplicates(nums):
    for i in range(len(nums)):
        while nums[i] == nums[i+1]:
            # i + 1 is duplicate, shift
            nums = nums[:i+1] + nums[i+2:]
    return len(nums)

nums = [1,1,2]
removeDuplicates(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
