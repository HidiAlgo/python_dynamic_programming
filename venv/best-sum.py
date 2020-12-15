#Time O(n^m * m)   Space O(m^2)
def bestSum1(targetSum,n):
    if targetSum == 0: return []
    if targetSum<0: return None

    shortestPath = None

    for num in n:
        remainder = targetSum - num
        remainderResult = bestSum1(remainder, n)
        if remainderResult != None:
            remainderResult.append(num)
            if(shortestPath == None or len(shortestPath) > len(remainderResult)):
                shortestPath = remainderResult

    return shortestPath


#Time O(n * m^2)   Space O(m^2)
def bestSum2(targetSum,n, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum<0: return None

    shortestPath = None

    for num in n:
        remainder = targetSum - num
        remainderResult = bestSum2(remainder, n, memo)
        if remainderResult != None:
            combination = remainderResult+[num]
            if(shortestPath == None or len(shortestPath) > len(remainderResult)):
                shortestPath = combination

    memo[targetSum] = shortestPath
    return shortestPath




print(bestSum2(100,[2,4,5,25]))
