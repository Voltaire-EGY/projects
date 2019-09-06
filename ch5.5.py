import random as r
a = set(r.choices(range(0,100), k=r.randint(10,50)))
b = set(r.choices(range(0,100), k=r.randint(10,50)))
c = list(a&b)
print(c)
