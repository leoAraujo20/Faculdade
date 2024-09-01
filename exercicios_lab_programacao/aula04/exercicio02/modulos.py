def union(list1, list2):
    if len(list1) >= len(list2):
        maior = list1
    else:
        maior = list2
    
    unity_list = []
    for i in range(len(maior)):
        if i > len(list1) - 1:
            unity_list.append(list2[i])
        else:
            unity_list.append(list1[i])
            unity_list.append(list2[i])
    
    return unity_list
