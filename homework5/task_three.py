users_input = input('Введите букву: ')
with open('C:/Users/user/homeworks/homework5/myfile.txt') as myfile:
    calc_n = 0

    for line in myfile:
        for i in line:
            if i == users_input:
                calc_n += 1
            elif i == users_input.swapcase():
                calc_n += 1

    print(calc_n)
