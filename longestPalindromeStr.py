s = 'aba'
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        # original_str = s
#         rev_str = s[::-1]
#         dic = {}
#         count = 0
        
#         if original_str == rev_str:
#             count += 1
#             dic[count] = rev_str
#             return rev_str
 
            
# def reducelength(o):
#     for i in range(len(o)):
#         if i != len(o)-1:
#             os = ''+o[i]
#     return os
# os=reducelength(s)
# longestPalindrome(os)
        result = ''
        for i in range(len(s)):
            result = max(get_str(s, i, i), get_str(s, i, i+1), result, key=len)
        return result

def get_str(s, left, right):
    while left >= 0 and len(s) > right and s[left] == s[right]:
        left -=1 
        right += 1
    return s[left+1:right]

print(longestPalindrome(s))