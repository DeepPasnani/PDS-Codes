i = int(input("Enter a first number: "))
j = int(input("Enter a second number: "))

o = input("Enter an operator (+, -, *, /): ")

if o == "+":
    print(i + j)
elif o == "-":
    print(i - j)
elif o == "*":
    print(i * j)
elif o == "/":
    print(i / j)
else:
    print("Invalid operator.")
