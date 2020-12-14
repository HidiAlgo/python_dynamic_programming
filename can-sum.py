#Time O(n^m)    Space O(m) where the targetSum = m
def canSum1(targetSum, n):
    if targetSum == 0: return True
    if targetSum<0: return False

    for num in n:
        remainder = targetSum - num
        if canSum1(remainder, n): return True

    return False

#Time O(m*n)    Space O(m) where the targetSum = m
def canSum2(targetSum, n, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum<0: return False

    for num in n:
        remainder = targetSum - num
        if(canSum2(remainder, n, memo)):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False



print(canSum2(300, [7, 14]))