def lessThan4(aList):
    """
    makes a list of words of length less than 4
    """
    lessThan4List = []
    for word in aList:
        if len(word) < 4:
            lessThan4List.append(word)
    return lessThan4List
    
#print lessThan4(["apple", "cat", "dog", "banana"])