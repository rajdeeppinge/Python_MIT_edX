s = raw_input("Enter input ")
count = 0
for vowel in s:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        count += 1
print "Number of vowels:", count