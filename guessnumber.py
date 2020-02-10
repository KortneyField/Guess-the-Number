import random



guessNum = 0
guessLimit = 3

print(" ")
print("     ***Welcome to the Great Number Guessing Game***")
print(" ")

low = int(input("Enter low number: "))
high = int(input("Enter high number: ")) 

num = random.randint(low,high)

while True:
    guess = int(input("guess number:"  ))
    print(" ")
    if guess == num:
        print("CONGRATS!! You guess the number! ")
        print(" ")
        break
    else:
        guessNum = guessNum + 1
        print("SORRY not it, try again")
        print("You have {} guesses left".format(guessNum))
        print(" ")
        pass
