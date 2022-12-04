user_index = int(input('Введите индекс: '))

number1 = 0
number2 = 1
index = 1
while True:
    index += 1
    new_number = number1 + number2
    number1 = number2
    number2 = new_number

    if user_index == index:
        print(f'Результат: число Фибоначчи = {new_number}')
        break
    elif user_index == 0:
        print(f'Результат: число Фибоначчи = {number2 - 1}')
        break
    elif user_index == 1:
        print(f'Результат: число Фибоначчи = {number2}')
        break
