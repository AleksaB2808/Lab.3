# Lab.3
Функція task1

def task1(my_list):
    my_list.insert(1, -5)  # Вставляє число -5 на позицію з індексом 1 у вхідний список my_list

    min_element = min(my_list)  # Знаходить мінімальне значення у списку my_list
    max_element = max(my_list)  # Знаходить максимальне значення у списку my_list

    my_list.insert(2, [1, 2, 3])  # Вставляє список [1, 2, 3] на позицію з індексом 2 у вхідний список my_list

    my_list.append(["Проценко", "Ярослав"])  # Додає список ["Проценко", "Ярослав"] в кінець вхідного списку my_list

    list_length = len(my_list)  # Знаходить довжину списку my_list

    print("my_list:", my_list)  # Друкує список my_list
    print("min_element:", min_element)  # Друкує мінімальний елемент my_list
    print("max_element:", max_element)  # Друкує максимальний елемент my_list
    print("list_length:", list_length)  # Друкує довжину my_list

    return my_list, min_element, max_element, list_length  # Повертає кортеж зі значеннями my_list, мінімальним і максимальним елементами та довжиною my_list
Опис:

Вставка числа -5 на позицію з індексом 1 у вхідний список my_list.
Знаходження мінімального значення у списку my_list.
Знаходження максимального значення у списку my_list.
Вставка списку [1, 2, 3] на позицію з індексом 2 у вхідний список my_list.
Додавання списку ["Проценко", "Ярослав"] в кінець вхідного списку my_list.
Знаходження довжини списку my_list.
Друк списку my_list, мінімального і максимального елементів і довжини списку.
Повертає кортеж з вхідним списком my_list, мінімальним і максимальним елементами і довжиною списку my_list.
Функція task2

def task2(A, B, C):
    total_cost = sum([quantity * price for quantity, price in zip(B, C)])  # Обчислення загальної вартості товарів
    average_price = sum(C) / len(C)  # Обчислення середньої ціни товарів
    most_stocked_index = B.index(max(B))  # Знаходження індексу товару з найбільшою кількістю на складі
    most_stocked_item = A[most_stocked_index]  # Знаходження товару з найбільшою кількістю на складі
    return total_cost, average_price, most_stocked_item  # Повертає кортеж зі значеннями total_cost, average_price і most_stocked_item
Опис:

Обчислення загальної вартості товарів, перемножуючи кількість (зі списку B) на ціну (зі списку C) для кожної пари товару.
Обчислення середньої ціни товарів у списку C.
Знаходження індексу товару з найбільшою кількістю на складі (максимальне значення у списку B).
Знаходження товару з найбільшою кількістю на складі (використовуючи індекс most_stocked_index у списку A).
Повертає кортеж із значеннями total_cost (загальна вартість), average_price (середня ціна) і most_stocked_item (товар з найбільшою кількістю на складі).
Функція task3

def task3():
    # Створення списку із чисел від -25 до 25
    my_list = list(range(-25, 26))

    A1 = []  # Порожній список для позитивних чисел
    A2 = []  # Порожній список для негативних чисел

    for i in my_list:
        if i > 0:
            A1.append(i)  # Додавання позитивного числа до A1
        else:
            A2.append(i)  # Додавання негативного числа до A2

    return A1, A2  # Повертає кортеж із списками позитивних і негативних чисел
Опис:

Створення списку my_list з чисел від -25 до 25.
Ініціалізація порожніх списків A1 і A2 для позитивних і негативних чисел відповідно.
Проходження по кожному числу i у списку my_list.
Якщо i більше 0, то i додається до списку A1.
Інакше i додається до списку A2.
Повертається кортеж із списками A1 (позитивні числа) і A2 (негативні числа).
