s = raw_input("Enter input ")
i = 0
long = 1
longest = None
startIndex = 0

while i < len(s):
    long = 1
    
    for j in range(i+1, len(s)):
        if s[j-1] <= s[j]:
            long += 1
        else: break
    
    if longest is None:
        longest = long
    elif long > longest:
        longest = long
        startIndex = i
        
    i += long
    
print "Longest substring in alphabetical order is:", s[startIndex:startIndex+longest]