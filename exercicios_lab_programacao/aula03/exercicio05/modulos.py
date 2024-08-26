def payment(salary,quant):
    value = salary + quant * 0.5
    return value

def category(value):
    if value <= 1000:
        return 'A'
    elif value <= 1500:
        return 'B'
    elif value <= 2000:
        return 'C'
    else:
        return 'D'
    
def lowest(value, new_value):
    if value >= new_value:
        return True
    return False
