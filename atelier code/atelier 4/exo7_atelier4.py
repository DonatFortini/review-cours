##question 1
import random

def stupid_sort(list_to_sort:list)->list:
    while list_to_sort != list_to_sort.sort():
        random.shuffle(list_to_sort)


