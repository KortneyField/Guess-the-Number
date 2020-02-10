import random


num = random.randint(1,5)


print(" ")
print("     ***Welcome to the Great Number Guessing Game***")
print(" ")


while True:
    guess = int(input("guess number:"  ))
    if guess == num:
        print("Congradulations. You guess the number! ")
    else:
        print("Sorry not it, try again")
        pass
