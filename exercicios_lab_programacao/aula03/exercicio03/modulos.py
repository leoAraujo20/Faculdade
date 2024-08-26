def indemnity(house_class,m2):
    if house_class == 'A':
        return 500 * m2
    return 300 * m2

def bigger(value,new_value):
    if new_value >= value:
        return new_value
    return value
    