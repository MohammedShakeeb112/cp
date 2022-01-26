def romanToInt(s):
    # print(s)
    # print(len(s))
    letter = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if 1<= len(s) <= 15:
        intValue = 0
        for i in range(len(s)-1):
            if letter[s[i]] < letter[s[i+1]]:
                intValue -= letter[s[i]]
            else:
                intValue += letter[s[i]]
    else: 
        return 'Invalid Value passed'
    return intValue + letter[s[-1]]
s = 'VI'
print(romanToInt(s))
