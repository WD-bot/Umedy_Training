import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(0)
        except: #or ValueError (more specific) or Exeption but is less specific
            print("Invalid number, please try again")
        finally: #ALWAYS EXECUTED
            print("the finally clause always exercutes")

# a=int(input("Type a number"))
# b=int(input("Type the number you want to divide it by"))
first_number = getint("Please enter first number")
second_number = getint("Please enter second number")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number/second_number))
except ZeroDivisionError:
    print("You cannot divide a number with zero")
    sys.exit(2)#will give an exit code when "used"
else:
    print("Successful division")
