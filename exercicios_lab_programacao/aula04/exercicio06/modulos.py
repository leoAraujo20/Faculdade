def biggest(list):
    
    bigger_lines = []
    bigger = 0
    for i in list:
        for j in i:
            if j >= bigger:
                bigger = j
        bigger_lines.append(bigger)
    
    max = 0
    for i in bigger_lines:
        if i >= max:
            max = i
    
    return f' Biggest numbers in each line {bigger_lines}, biggest number: {max}'
