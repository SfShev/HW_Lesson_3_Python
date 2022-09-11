# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def new_list (x):
    _list = []
    for i in range(x):
        _list.append(int(input(f"Введите число {i + 1}: ")))
    print(f"Ваш список: {_list}")    
    return _list  

def sum_odd_index(_list):

    new_list = _list[1::2]
    sum = 0
    for i in range(len(new_list)):
        sum = sum + new_list[i]

    return print(sum)


quantity = int(input("Сколько чисел будет в списке: "))
_list = new_list(quantity)
sum_odd_index(_list)
