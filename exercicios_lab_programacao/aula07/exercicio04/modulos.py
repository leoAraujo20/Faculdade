def calculate_average(original_list:list):
    
    total_sum = sum(original_list)
    jump_average = total_sum / len(original_list)
    return jump_average

def print_list(original_list):
    
    for value in original_list:
        print(value, end='-')