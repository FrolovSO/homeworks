operator = {
    '44': 'A1',
    '291': 'A1',
    '293': 'A1',
    '296': 'A1',
    '299': 'A1',
    '33': 'MTC',
    '297': 'MTC',
    '295': 'MTC',
    '298': 'MTC',
    '292': 'MTC',
    '25': 'life:)'
}
cuntry_code = '375'

while True:
    result = {}

    error = False
    users_input = input('Введите номер телефона в международном формате : ')

    if len(users_input) != 13:
        result['success'] = False
        result['dscription'] = "Номер должен быть длиной 13 символов."
        error = True

    for char in users_input[1:14]:
        if not char.isdigit():
            result['success'] = False
            result['dscription'] = "Первый символ знак плюс, остальные цифры"
            error = True
            break

    if users_input[1:4] != cuntry_code:
        result['succes'] = False
        result['description'] = "Код страны должен быть равен 375"
        error = True

    if users_input[0] not in ('+'):
        result['success'] = False
        result['dscription'] = "Первый символ знак плюс."
        error = True

    if users_input[4:6] in ('33', '44', '25'):
        find_operator = operator[users_input[4:6]]
    else:
        find_operator = operator[users_input[4:7]]

    if error:
        print(result)
    else:
        result['succes'] = True
        result['phone'] = users_input
        result['operator'] = find_operator
        print(result)

    exit_choice = input("Хотите выйти из программы(Y/n): ")
    if exit_choice == "y":
        break
