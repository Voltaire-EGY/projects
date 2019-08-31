x = int(input("Enter a number: "))
a = list(range(1, x))
b = []
for item in a:
    if x%item is 0:
        b.append(item)
print(b)
