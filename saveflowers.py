data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = "flowers_print.txt"

# with open(plants_filename,"w") as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# #writing data to a file
#
# new_list= []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
# print(new_list)

# plants_filename="flowers_write.txt"
#
# with open(plants_filename,"w") as plants:
#     for plant in data: #iterates over the list
#         plants.write(plant) #write them in another file
# print(data)
# string_reprensentation = data.__str__()
# print(type(string_reprensentation))

filename = "test_numbers.txt"
with open(filename,"w") as test:
    for i in range(10):
        print(i, file=test)

with open(filename,"w") as test:
    for i in range(10):
        test.write(str(i)+"\n")
