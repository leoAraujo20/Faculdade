from random import randint

def create_random_list(list_range):
    my_list = [randint(0,10) for x in range(list_range)]
    return my_list