# 28. Implement strStr()

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:

# Input: haystack = "", needle = ""
# Output: 0

 

# Constraints:

#     0 <= haystack.length, needle.length <= 5 * 104
#     haystack and needle consist of only lower-case English characters.

def strStr(haystack, needle):
    # if needle == "":
    #     print(0)
    # if needle not in haystack:
    #     print(-1)
    # else :
    #     print(len(needle))
    
    # if len(haystack) < len(needle): 
    #     return -1
    # if not needle:
    #     return 0
    
    # i = j = 0
    # while j < len(needle) and i < len(haystack): 
    #     if haystack[i] != needle[j]:
    #         i = i - j + 1
    #         j = 0
    #         continue 
    #     i += 1
    #     j += 1
    # return i - j if j == len(needle) else -1


    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1




haystack, needle = "", ""

print(strStr(haystack, needle))