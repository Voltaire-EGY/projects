n = input("Enter your name: ")
a = int(input("Enter your age: "))
a_100 = 2019 - a + 100
a_100 = str(a_100)
r = int(input("Enter a number of repetition: "))
x = 0
while x < r:
    print("Hi " + n + ", you will be 100 years old in " + a_100)
    x = x +1
