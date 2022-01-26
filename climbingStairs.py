# 70. Climbing Stairs
# Easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

 

# Constraints:

#     1 <= n <= 45
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbingStairs(self, n):
        # step1 = 1
        # step2 = 2
        # pos = 0
        

        # for i in range(n):
        #     if step1 + step1 + step1 == n:
        #         pos += 1
        #     elif step1 + step2 == n:
        #         pos += 2
        # return pos

        # for i in range(n):
        #     if step1*n ==n:
        #         pos += 1
        #     elif step1*(n//2) + step2 == n:
        #         pos += 3
        #     elif step2*(n//2) == n:
        #         pos += 1
        # return pos
        

        # if 1 <= n <= 45:
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     return climbingStairs(n-1) + climbingStairs(n-2) 
        # return 'n should be either less than or equal to 45'

        if 1 <= n <= 45:
            if n not in self.dic:
                self.dic[n] = self.climbingStairs(n-1) + self.climbingStairs(n-2)
            return self.dic[n]
        return f'{n} should be either less or equal to 45'

s = Solution()
n=46
print(s.climbingStairs(n))