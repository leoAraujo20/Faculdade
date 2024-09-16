def count_votes(orignal_list:list):
    
    count_votes = []
    for i in range(1, 7):
        count_votes.append(orignal_list.count(str(i)))
    return count_votes

def percentage(original_list:list, sum_list:list):
    
    percen_list = []
    for value in sum_list:
        value_percen = (value / len(original_list)) * 100
        percen_list.append(value_percen)
    return percen_list