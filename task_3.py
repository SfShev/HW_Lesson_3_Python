# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

def new_list (x):
    _list = []
    for i in range(x):
        _list.append(float(input(f"Введите вещественное число {i + 1}: ")))
    print(f"Ваш список: {_list}")    
    return _list 


def difference_min_max(x):
    _list=[]
    fractional = 0
    result=0
    for i in range(len(x)):
        fractional = x[i] % 1
        _list.append(fractional)
    result = round(max(_list)- min(_list), 4 )
    return result
quantity = int(input("Сколько чисел будет в списке: "))
_list = new_list(quantity)
print(difference_min_max(_list))