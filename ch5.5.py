from random import choices, randint
a = set(choices(range(0,100), k=randint(10,50)))
b = set(choices(range(0,100), k=randint(10,50)))
c = list(a&b)
print(c)
