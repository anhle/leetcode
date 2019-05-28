"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def twoSum(nums, target) :
    # Time: O(n)
    # Space: O(n)
    n = len(nums)
    if n <= 1:
        return False
    buf_dict ={}
    for i in range(n):
        complement = target - nums[i]
        if complement in buf_dict:
            return [buf_dict[complement],i]
        else:
            buf_dict[nums[i]]=i

print(twoSum([2,7,11,15],9))