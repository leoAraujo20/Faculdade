def pair(list):
    
    pair_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            pair_list.append(list[i])
    
    return pair_list