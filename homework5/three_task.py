with open('three_task.txt') as f:
    user = input('Введите букву: ')
    user2 = user.lower()
    text = f.read()
    text2 = text.lower()
    print(f'Результат: буква встречается {text2.count(user2)} раз в тексте.')
