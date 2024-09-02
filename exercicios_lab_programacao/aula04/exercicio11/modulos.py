def has_duplicates(list):
    for value in list:
        value_count = list.count(value)
        if value_count > 1:
            return True
    return False