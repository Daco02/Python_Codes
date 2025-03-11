# Write a program to calculate sum of the following series: 1+2+3+...+n

def sum(n):
    a = 0
    for i in range(1, n + 1):
        a += i
    return a

n = int(input("Enter a number: "))

print("Sum of series:", sum(n))
