# 169. Majority Element
# Easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

 

# Constraints:

#     n == nums.length
#     1 <= n <= 5 * 104
#     -231 <= nums[i] <= 231 - 1

 
# Follow-up: Could you solve the problem in linear time and in O(1) space?


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dic = {}
    # count = 0
    # for i in range(len(nums)):
    #     if nums[i] in dic.keys():
    #         dic[nums[i]] = dic[nums[i]] + 1
    #     else:
    #         dic[nums[i]] = count +1

    nums.sort()
    # print(len(nums)//2)
    return (nums[len(nums)//2])    

    

nums = [3,4,3]
print(majorityElement(nums))