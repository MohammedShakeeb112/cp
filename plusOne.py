# 66. Plus One
# Easy

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:

# Input: digits = [0]
# Output: [1]
# Explanation: The array represents the integer 0.
# Incrementing by one gives 0 + 1 = 1.
# Thus, the result should be [1].

# Example 4:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

 

# Constraints:

#     1 <= digits.length <= 100
#     0 <= digits[i] <= 9
#     digits does not contain any leading 0's.

def plusOne(digits):
    # digits[-1] = digits[-1]+1
    # return digits
    # if digits[-1] > 9:
    #     digits[-1] = str(digits[-1]).split()
    #     digits[-1] =  int(digits[-1][-1][-1])
    #     digits[-2] = digits[-2]+1
    #     return digits

    # return str(digits[-1])[0]
    # digits[-1] = digits[-1]+1
    # digit = []
    # if digits[-1] > 9:
    #     # for i in digits:
    #     rem = digits[-1]%10
    #     val = digits[-1]//10
    #     digit.append(val)
    #     digit.append(rem)
    #     return digit
        
    # return digits


    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]

digits = [9,9]
print(plusOne(digits))