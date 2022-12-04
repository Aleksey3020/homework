code = {'25': 'life:)',
        '291': 'А1',
        '292': 'МТС',
        '293': 'А1',
        '295': 'МТС',
        '296': 'А1',
        '297': 'МТС',
        '298': 'МТС',
        '299': 'А1',
        '33': 'МТС',
        '44': 'А1'}

while True:
    result = {}
    error = False
    usser_input = input('Введите номер телефона с кодом оператора: ')
    if len(usser_input) != 13:
        result['success'] = False
        result['description'] = "Number shold contains only 13 symbol."
        error = True

    for char in usser_input[1:13]:
        if not char.isdigit():
            result['success'] = False
            result['description'] = "Number shold contains only integers."
            error = True
            break

    if usser_input[0] != '+':
        result['success'] = False
        result['description'] = "The first symbol of the number '+'."
        error = True

    if usser_input[1:4] != '375':
        result['success'] = False
        result['description'] = "Country code must be '375'."
        error = True

    if usser_input[4:6] not in ('25', '33', '44', '29'):
        result['success'] = False
        result['description'] = "Operator code is incorrect."
        error = True

    if error:
        print(result)
    else:
        result['success'] = True
        result['phone'] = usser_input
        if usser_input[4:6] == '29':
            result['operator'] = code[usser_input[4:7]]
        else:
            result['operator'] = code[usser_input[4:6]]
        print(result)

    exit_session = input('Хотите выйти из сеанс (Y/n): ')
    if exit_session == 'Y':
        break
