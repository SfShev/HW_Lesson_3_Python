# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def new_list (x):
    _list = []
    for i in range(x):
        _list.append(int(input(f"Введите число {i + 1}: ")))
    print(f"Ваш список: {_list}")    
    return _list  


def prod_list(x):
    _list= []
    prod = 0
    if len(x)%2 == 1:
        for i in range(len(x)//2 + 1):
            if i == 0:
                prod = x[i] * x[-1]
            else:
                prod = x[i] * x[-i -1]
            _list.append(prod)
    else:
        for i in range(len(x)//2 ):
            if i == 0:
                prod = x[i] * x[-1]
            else:
                prod = x[i] * x[-i -1]
            _list.append(prod)
    return _list

quantity = int(input("Сколько чисел будет в списке: "))
_list = new_list(quantity)
print(prod_list(_list))