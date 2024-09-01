def odd_even(list):
    
    odd = []
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
        
    return (odd, even)
