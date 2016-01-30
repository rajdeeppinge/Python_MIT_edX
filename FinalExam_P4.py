aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    tempDict = {}
    lst = []
    
    for key, value in aDict.items():
        if value not in tempDict.keys():
            tempDict[value] = key
        else:
            tempDict[value] = None

    for key, value in tempDict.items():
        if tempDict[key] != None:
            lst.append(value)
        
    lst.sort()
    
    return lst
    
print uniqueValues(aDict)