#Реализуйте алгоритм перемешивания списка.

origin_list = list(input('введите список: '))
import random
def mix_list(origin_list):
    list = origin_list[:]
    length_list = len(list)
    for i in range (0, length_list):
        index_random = random.randint(0, length_list-1)
        X = list[i]
        list[i] = list[index_random]
        list[index_random] = X
    return list
print(f'Перемешанный список: {mix_list(origin_list)}')