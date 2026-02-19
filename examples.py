def factorial(n):
    #n! can also be defined as n * (n-1):
    """calculates n! recursively"""
    if n <=1:
        return 1
    else:
        # print(n / 0)
        return n* factorial(n-1)
a=input("type a number")
b=input("type the number you want to divide it by")

try:
    print(factorial(999)) #works to 999
except (RecursionError, ZeroDivisionError, OverflowError):
    print("This program cannot calculate factorials that large or divide by zero")
# except ZeroDivisionError:
#     print("This program cannot divide by zero")

print("Program termination")