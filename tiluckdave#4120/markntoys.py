def maximumToys(prices, k):
    prices.sort()
    print(prices)
    tot = 0
    for ind, i in enumerate(prices):  
        if tot > k:
            break        
        tot += i
        count = ind
            
    if k >= tot:
        return len(prices)
    return count
