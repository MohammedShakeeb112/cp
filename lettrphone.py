def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits) == 0: return []
        if len(digits) == 1: return list(dic[digits[0]])
        first = letterCombinations(digits[:-1])
        last = list(dic[digits[-1]])
        result = []
        for i in first:
            for j in last:
                result.append(i+j)
        return result
print(letterCombinations('436'))