def oddoreven(a):
    if a.is_integer() is True:
        return "This number is even"
    else:
        return "This number is odd"

print(oddoreven(float(input("Enter a number: "))/2))
