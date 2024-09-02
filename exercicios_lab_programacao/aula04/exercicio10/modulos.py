def is_sorted(original_list):
    sorted_list = original_list.copy()
    sorted_list.sort()
    if original_list == sorted_list:
        return True
    return False