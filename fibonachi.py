def fib1(n):  #Time O(2^n)  Space O(n)
    if n<=2: return 1
    return fib1(n-1) + fib1(n-2)

def fib2(n, memo={}): #Time O(n)  Space O(n)
    if n in memo: return memo[n]
    if n<=2: return 1
    memo[n] = fib2(n-1, memo) + fib2(n-2, memo)
    return memo[n]

print(fib2(50))