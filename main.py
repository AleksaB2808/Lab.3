def task1(my_list):
    my_list.insert(1, -5)


    min_element = min(my_list)
    max_element = max(my_list)

    my_list.insert(2, [1, 2, 3])


    my_list.append(["Проценко", "Ярослав"])

    list_length = len(my_list)

    print("my_list:", my_list)
    print("min_element:", min_element)
    print("max_element:", max_element)
    print("list_length:", list_length)

    return my_list, min_element, max_element, list_length


initial_list = [4, 7, 2, 9]
result = task1(initial_list)

def task2(A, B, C):
    total_cost = sum([quantity * price for quantity, price in zip(B, C)])
    average_price = sum(C) / len(C)
    most_stocked_index = B.index(max(B))
    most_stocked_item = A[most_stocked_index]
    return total_cost, average_price, most_stocked_item

A = ["Товар1", "Товар2", "Товар3", "Товар4", "Товар5"]
B = [10, 15, 5, 20, 8]
C = [100, 200, 150, 120, 180]

result = task2(A, B, C)

def task3():
    # Сформуємо список із 50 елементів в діапазоні від -25 до 25
    my_list = list(range(-25, 26))

    A1 = []
    A2 = []

    for i in my_list:
        if i > 0:
            A1.append(i)
        else:
            A2.append(i)
    return A1, A2

result_A1, result_A2 = task3()

print(result_A1, result_A2)

def task4(my_string):
    # Підраховуємо кількість символів "а" у тексті
    count_a = my_string.count('а')

    # Повертаємо кількість символів "а"
    return count_a

# Приклад виклику функції
input_string = "Це тестовий текст, де ми рахуємо кількість 'а' символів."
result1 = task4(input_string)

# При потребі можна використовувати змінну result для отримання кількості символів "а"
def task5(my_string):
    # Замінюємо "GOOD" на "NICE" у рядку
    modified_str = my_string.replace("GOOD", "NICE")

    # Розподіляємо рядок по пробілу та обчислюємо кількість слів
    word_count = len(my_string.split())

    # Повертаємо значення modified_str та word_count
    return modified_str, word_count

# Приклад виклику функції
input_string = "GOOD morning! Have a GOOD day."
result_modified_str, result_word_count = task5(input_string)

# При потребі можна використовувати змінні result_modified_str та result_word_count для отримання результатів
def task6():
    # Створюємо список від 1 до 5
    my_list = [1, 2, 3, 4, 5]

    # Підсумовуємо всі елементи списку
    total_sum = sum(my_list)

    # Повертаємо значення total_sum
    return total_sum

# Приклад виклику функції
result_total_sum = task6()

# При потребі можна використовувати змінну result_total_sum для отримання результату
def task7(my_list):
    # Ініціалізуємо порожній список для результатів
    result = []

    # Проходимося по елементах у списку
    for num in my_list:
        # Перевіряємо, чи число ділиться на 7 і є кратним 5
        if num % 7 == 0 and num % 5 == 0:
            # Додаємо число до результатів
            result.append(num)

    # Повертаємо значення result
    return result

# Приклад виклику функції
input_list = [10, 14, 35, 21, 25, 30, 49]
result = task7(input_list)

# При потребі можна використовувати змінну result для отримання результату


