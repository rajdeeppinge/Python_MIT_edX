s = raw_input("Enter input ")
count = 0
for i in range(0, len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print "Number of times bob occurs is:", count