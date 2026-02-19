import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

loc = 1
forest = [locations[xit] for xit in exits if loc in exits[xit].values()]
print(forest)
print()

for loc in sorted(locations):
    forest = []
    for xit in exits:
        if loc in exits[xit].values():
            forest.append(locations[xit])
    print("Locations leading to {}".format(loc), end = '\t')
    print(forest)

print()
print("nested for loops")
print("________________")
nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exits_to_destination_1)
"""
print()
print("List comprehensions inside a for loop")
print("_____________________________________")
loop_comp = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits
                              if loc in exits[xit].values()]
    print("Locations leading to {}". format(loc), end='\t')
    print(exits_to_destination_2)
"""
print()
print("nested comprehensions")
print("_____________________")
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] 
                            for loc in sorted(locations)]
print(exits_to_destination_3)
print()
for index, loc in enumerate(exits_to_destination_3):
    print("Locations leading to: {}".format(index), end='\t')
    print(loc)
"""
#timed tests
result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
print("Nested loop: \t{}".format(result_1))