a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

new_a = {}
for key, value in a.items():
    for key_two, value_two in b.items():
        if key == key_two:
            new_a[key] = [value, value_two]
        else:
            new_a[key] = [value, None]
new_b = {}
for key, value in b.items():
    for key_two, value_two in a.items():
        if key == key_two:
            new_b[key] = [value, value_two]
        else:
            new_b[key] = [None, value]

new_a.update(new_b)
print(f'ab = {new_a}')
