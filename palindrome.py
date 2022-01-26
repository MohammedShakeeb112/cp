def palindrome(x):
    num = list(str(x))
    # print(num)
    rev_num = []
    
    for i in range(len(num)):
        po = num.pop(-1)
        rev_num.append(po)
    
    # print(str(x))
    # print(rev_num[:])
    rev_str = ""
    for i in rev_num:
        rev_str += i
    # print(rev_str)
    
    if rev_str == str(x):
        return True
    else:
        return False

# nums = -540
nums = 101
print(palindrome(nums))