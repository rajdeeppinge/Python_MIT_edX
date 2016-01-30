def keysWithValue(aDict, target):
    reqdKeyList = []
    for key in aDict:
        if aDict[key] == target:
            reqdKeyList.append(key)
            
    reqdKeyList.sort()
    return reqdKeyList
        
#print keysWithValue({10:1, 30:2, 20:2}, 2)