from operator import itemgetter

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# meals = [meal if "spam" not in meal else "a meal is skipped" for meal in menu] #expression first "meal if "spam" not in meal else "a meal is skipped""
# ##iteration later " for meal in menu"
# print(meals)
#
# x = 1
# expression = "twelve" if x == 12 else "unknown"
# print(expression)

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal
    else "contains bacon" if "bacon" in meal
    else "contains egg" if "egg" in meal
    else "contains neither sausage, bacon nor egg")

print()

items =  set ()
for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break

for x in range (1,31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3==0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)