i = int(input("Enter the number of terms for the Fibonacci series: "))
a, b = 0, 1

for z in range(i):
    print(a, end=" ")
    a = b
    b = a + b
