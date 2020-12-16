#TIme O(n^m * m)   Space(m^2)
def countConstruct1(target, wordBank):
    if target == "": return 1

    total = 0;
    for word in wordBank:
        if(target.find(word) == 0):
            suffix = target[len(word):]
            way = countConstruct1(suffix,wordBank)
            total += way

    return total

#TIme O(n * m^2)   Space(m^2)
def countConstruct2(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == "": return 1

    total = 0;
    for word in wordBank:
        if(target.find(word) == 0):
            suffix = target[len(word):]
            way = countConstruct2(suffix,wordBank,memo)
            total += way

    memo[target] = total
    return total

print(countConstruct2("purple",["purp","p","ur","le"]))
print(countConstruct2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                    ["ee", "eeee", "eeeee", "eeeeee", "eeeeeee"]))