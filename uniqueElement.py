def findOnce(nums):
    
        size = len(nums)
        
        left, right = 0, size // 2
        
        while left < right:
            
            pair_index = left + ( right - left ) // 2
            
            if nums[2*pair_index] != nums[2*pair_index+1]:
                # If current pair is mis-matched
                # then go left-half to find the first pair of mis-match
                right = pair_index
            
            else:
                # If current pair is with the same number appeared twice
                # then go right-half to find the first pair of mis-match
                left = pair_index + 1
        
        # when the while loop terminates, left = right = the first pair index of mis-match
        return nums[2*left]


#METHOD II
from functools import reduce
def singleNonDuplicate(nums):
    return reduce(lambda x, y: x^y, nums, 0)
        
arr = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]

# findOnce(arr)
singleNonDuplicate(arr)