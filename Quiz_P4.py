def myLog(x, b):
    """
    function to find floor(log x to the base b)
    """
    i = 0
    while b**i <= x:
        i += 1
        
    return i-1
    
#print myLog(13, 3)