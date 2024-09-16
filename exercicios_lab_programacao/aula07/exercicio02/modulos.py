def print_list(original_list):
    
    for value in original_list:
        print(value, end=' ')

def reverse_list(original_list:list):
    
    reverse_list = original_list.copy()
    reverse_list.reverse() 
    for value in reverse_list:
        print(value)

def total_sum(original_list):
    
    total_sum = sum(original_list)
    return total_sum

def calculate_average_grade(original_list:list):
    
    total_sum = sum(original_list)
    grade_average = total_sum / len(original_list)
    return grade_average

def above_average(original_list, average):
    for value in original_list:
        if value > average:
            print(value)

def above7(original_list):
    for value in original_list:
        if value > 7:
            print(value)