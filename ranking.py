def binom(n, k):
    if n < k:
        return 0
    
    m = min(k, n - k)
    result = 1
    
    for i in range(m):
        result *= (n - i)
        result //= (i + 1)
        
    return result

def rank(C):
    i = len(C)
    result = 0
    
    for c in C:
        result += binom(c, i)
        i -= 1
        
    return result

def largest_binom_below_index(i, k):
    last_m, last_binom_m = 0, 0
    m = k - 1
    binom_m = 0
    
    while binom_m <= i:
        last_m = m
        last_binom_m = binom_m
        m += 1
        binom_m = binom(m, k)
        
    return last_m, last_binom_m

def unrank(i, n, k):
    if i >= binom(n, k):
        return None
    
    if k == 1:
        return [ i ]

    m, binom_m = largest_binom_below_index(i, k)
        
    return [ m ] + unrank(i - binom_m, m, k - 1)