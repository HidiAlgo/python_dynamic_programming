#TIme O(n^m * m)   Space(m^2)
def canConstruct1(target, words):
    if target == "": return True

    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if(canConstruct1(suffix,words)): return True

    return False


#TIme O(n * m^2)   Space(m^2)
def canConstruct2(target, words, memo={}):
    if target in memo: return memo[target]
    if target == "": return True

    for word in words:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if(canConstruct2(suffix,words, memo)):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canConstruct2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                    ["ee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))
# print(canConstruct1("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#                     ["ee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))
