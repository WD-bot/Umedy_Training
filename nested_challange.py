for i in range(1,11):
    for j in range(1,11):
        print(1, i*j)


times = [(i, i*j) for i in range(1,11) for j in range(1,11)]
print(times)

for x,y in [(i, i*j) for i in range(1,11) for j in range(1,11)]:
    print(x,y)

times2 = [[(i, i*j) for i in range(1,11)] for j in range(1,11)]
print(times2)

for x,y in ((i, i*j) for i in range(1,11) for j in range(1,11)):
    print(x,y)