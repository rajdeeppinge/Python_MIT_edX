def sumDigits(N):
    if N <= 0:
        return 0
    sum = 0
    sum += N%10 + sumDigits(N/10)
    return sum
    
#print sumDigits(567)