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

def to_one_index(x):
    if type(x) == int:
        return x + 1
    if type(x) == list:
        return [ e + 1 for e in x ]
    
def to_zero_index(x):
    if type(x) == int:
        return x - 1
    if type(x) == list:
        return [ e - 1 for e in x ]
    
def rank_one_index(C):
    return to_one_index(rank(to_zero_index(C)))

def unrank_one_index(i, n, k):
    return to_one_index(unrank(to_zero_index(i), n, k))