def rev_int(x):
    num = abs(x)
    sign = 1
    rev_num = 0

    while num > 0:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10

    if x < 0:
        sign = -1
    rev_num = rev_num * sign
    if -(2**31)-1 < rev_num < 2**31:
        return rev_num
    else:
        return 0

print(rev_int(-110))