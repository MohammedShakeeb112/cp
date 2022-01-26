# 15. 3Sum
# Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:

# Input: nums = []
# Output: []

# Example 3:

# Input: nums = [0]
# Output: []

 

# Constraints:

#     0 <= nums.length <= 3000
#     -105 <= nums[i] <= 105

# print('1')
def threeSum(nums):
    # res = []
    # nums.sort()
    
    # for i in range(len(nums)-2):
    #     if i > 0 and nums[i] == nums[i-1]:
    #         continue
    #     l, r = i+1, len(nums)-1
    #     while l < r:
    #         Sum = nums[i] + nums[l] + nums[r]
            
    #         if Sum < 0:
    #             l += 1
    #         elif Sum > 0:
    #             r -=1
    #         else:
    #             res.append((nums[i],nums[l],nums[r]))
    #             while l < r and nums[l] == nums[l+1]:
    #                 l += 1
    #             while l < r and nums[r] == nums[r-1]:
    #                 r -= 1
    #             l += 1
    #             r -= 1
    # return res



        nums.sort()
        num = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums) - 1
            while left < right:
                totalSum = nums[i] + nums[left] + nums[right]
                
                if totalSum < 0:
                    left += 1
                elif totalSum > 0:
                    right -= 1
                else:
                    num.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return num
nums = [-1,0,1,2,-1,-4]
# nums = []
# nums = [0]
print(threeSum(nums))