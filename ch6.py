txt = list(input("Enter a text to test if it is palindrome: \n"))
print("This is palindrome!") if txt == txt[::-1] else print("Not palindrome!")
