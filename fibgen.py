def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current

fib = fibonacci()

# for f in fib:
#     print(f) # DONT DO THIS INFINITE LOOP

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))