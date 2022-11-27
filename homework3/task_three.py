from random import randint

random_lst = [randint(-100, 100) for i in range(10)]

print(random_lst)

random_lst.insert(2, randint(-100, 100))

del random_lst[6]

print(random_lst)
