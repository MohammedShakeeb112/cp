def nextGreaterElement(n):
        """
        :type n: int
        :rtype: int
        """
        revDigit = 0
        renewN = n
        while renewN > 0:
            rem = renewN%10
            revDigit = revDigit*10+rem
            renewN = renewN//10
        if revDigit > n:
            return revDigit
        else:
            return -1 

# print(nextGreaterElement(101))

# print(~12) # ~ => complement
# print('Explanation')
# print("12 binary numbar is : 00001100")
# print("12's complement is : 11110011 = -13")

# print("13 binary : 00001101")
# print("2's complement : 1's complement +1")
# print("13's complement : 11110010")
# print("13 2's complement : 11110011 = -13")

# a = 10
# b = 5
# print(a&b)
# print(a|b)
# print(a and b)
# print(a or b)
# print(a^b)
# print(a<<b) #left shift
# print(a>>b) #right shift
# print(bin(2)) #binary number

# print(bin(1000))
# print(bin(~10))
# print(int(0b1010))

# bitwise complement=>  ~
# ~x = -x-1 #general formula
# print(~21)  # ~21 = -21-1 = -22
# a= 20
# print(~a)
# print(bin(a+1))
# print(bin(~(a+1)+1))


def gen(n):
    s = list(map(int,str(n)))
    print(s)
    i = len(s) - 1
    print(i)
    while i -1 >0 and s[i] <=s[i-1]:
        i -= 1

    if i==0:
        return -1
        
    j = i
    while j+1<len(s) and s[j+1]>s[i-1]:
        j += 1
    s[i-1], s[j] = s[j], s[i-1]
    s[i:] = reversed(s[i:])
    ret = int(''.join(map(str, s)))
        
    return ret if ret<=((1<<31)-1) else -1
# print(gen(54))

def count(self,arr, n, x):
		# code here
        countsum = 0
        for i in range(n):
            if(x==arr[i]):
                countsum += 1
            else:
                return 0
        return countsum