user_index_number = int(input('Введите индекс (целое положительно число): '))
a = 0
b = 1
index = 1

while True:
    if user_index_number == 0:
        print(f'Пользователь ввёл индекс {user_index_number}')
        print(f'Результат: число Фибоначчи = {a}')
        break
    elif user_index_number == 1:
        print(f'Пользователь ввёл индекс {user_index_number}')
        print(f'Результат: число Фибоначчи = {b}')
        break

    index += 1
    new_number = a + b
    a = b
    b = new_number

    if index == user_index_number:
        print(f'Пользователь ввёл индекс {user_index_number}')
        print(f'Результат: число Фибоначчи = {new_number}')
        break
