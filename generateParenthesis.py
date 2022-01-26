def generateParenthesis(n):
    # def generate(p, left, right, parens=[]):
    #     if left:         generate(p + '(', left-1, right)
    #     if right > left: generate(p + ')', left, right-1)
    #     if not right:    parens += p,
    #     return parens
    # return generate('', n, n)

    allOutput = []
    def dfs(output, numOfLeft, numOfRight, n):
        if len(output) == n * 2:
            allOutput.append(output)
            return
        if numOfLeft < n:
            dfs(output + '(', numOfLeft + 1, numOfRight, n)
        if numOfLeft > numOfRight and numOfRight < n:
            dfs(output + ')', numOfLeft, numOfRight + 1, n)
    dfs('(', 1, 0, n)
    return allOutput
n = 3
print(generateParenthesis(n))