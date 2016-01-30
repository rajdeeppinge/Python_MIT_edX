def satisfiesF(L):
    lst = L[:]
    for str in lst:
        if not f(str):
            L.remove(str)
    
    return len(L)
    
def f(s):
    return s == 'abcd'
      
L = ['abcd', 'bsds', 'fsr', 'yyyy', 'abcd', 'abcde']

print satisfiesF(L)
print L