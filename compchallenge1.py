# for x in range (1,31):
#     fizzbuzz = "fizz buzz" if x % 15 == 0 \
#         else "fizz" if x % 3==0 \
#         else "buzz" if x % 5 == 0 else str(x)
#     print(fizzbuzz)

fizzbuzz = ["fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0
            else "buzz" if x % 5 == 0 else str(x)
            for x in range(1,31)]
print(fizzbuzz)

for buzz in fizzbuzz:
    print(buzz.center(12, '-'))

