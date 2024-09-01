def average(list):

    average_each_line = []
    for i in list:
        sum_in_lines = 0
        cont = 0
        for j in i:
            cont += 1
            sum_in_lines += j
        average_lines = sum_in_lines / cont
        i.append(round(average_lines,2))
        average_each_line.append(round(average_lines,2))


    max_sum = 0
    cont = 0
    for i in average_each_line:
        cont += 1
        max_sum += i
    
    max_average = max_sum / cont
    list.append(round(max_average,2))
        

    return list
    
    
        
