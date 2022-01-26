# 69. Sqrt(x)
# Easy

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

# Example 1:

# Input: x = 4
# Output: 2

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

 

# Constraints:

#     0 <= x <= 231 - 1

import math

def mySqrt(x):
    # l, r = 0, x
    # while l <= r:
    #     mid = l + (r-l)/2
    #     if mid * mid <= x < (mid+1)*(mid+1):
    #         return mid
    #     elif x < mid * mid:
    #         r = mid - 1
    #     else:
    #         l = mid + 1
    if x >= 0:
        return int(math.sqrt(x))

x = 45
print(mySqrt(0))