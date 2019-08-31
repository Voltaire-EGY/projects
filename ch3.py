a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
x = int(input("Enter a number: "))
for item in a:
    if item < x:
        b.append(item)
print(b)
