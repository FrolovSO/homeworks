console_string = input('вводите имя и фамилию в консоль: ')

console_string = console_string.split(' ')
console_string = console_string[::-1]
console_string = ' '.join(console_string)

print(console_string)
