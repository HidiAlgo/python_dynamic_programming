def grid_traveller1(m, n): #Time O(2^n+m)   Space O(n+m)
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return grid_traveller1(m-1,n) + grid_traveller1(m, n-1)

def grid_traveller2(m,n, memo={}): #Time O(n*m)   Space O(n+m)
    key = str(m)+","+str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = grid_traveller2(m-1,n, memo) + grid_traveller2(m,n-1, memo)
    return memo[key]

print(grid_traveller2(18,18))
