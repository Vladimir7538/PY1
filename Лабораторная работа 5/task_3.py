import random


def get_unique_list_numbers() -> list[int]:
    len_of_list = 15
    list_ = []

    while True:
        list_.append(random.randint(-10, 10))
        set_ = set(list_)
        if len(set_) == len_of_list:
            return list(set_)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
