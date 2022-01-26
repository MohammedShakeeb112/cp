# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lower-case English letters.

# def longestCommonPrefix(strs):     
#         if not strs:
#             print(strs)



def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        shortest = min(strs,key=len)
        # print(shortest)
        for i, ch in enumerate(shortest):
            print(i,ch)
            print('-------')
            for other in strs:
                print(other)
                # if other[i] != ch:
                #     return shortest[:i]
        return shortest 

strs = ['globe', 'flow', 'water']
longestCommonPrefix(strs)