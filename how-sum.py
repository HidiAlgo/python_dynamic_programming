#Time O(n^m * m)   Space O(m) where n = length of the numbers array, m = targetSum
def howSum1(targetSum, n):
    if targetSum == 0: return []
    if targetSum<0: return None

    for num in n:
        remainder = targetSum - num;
        remainderResult = howSum1(remainder, n)
        if remainderResult != None:
            remainderResult.append(num)
            return remainderResult

    return None

#Time O(n*m^2) ,Space O(m*m) where n = length of the numbers array, m = targetSum
def howSum2(targetSum, n, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum<0: return None

    for num in n:
        remainder = targetSum - num
        remainderResult = howSum2(remainder, n, memo)
        if remainderResult != None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return remainderResult

    memo[targetSum] = None
    return None
print(howSum2(300,[7,14]))