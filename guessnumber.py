import random



guessNum = 0
guessLimit = 3
low = 0
high = 20
num = random.randint(low,high)

#low = int(input("Enter low number: "))
#high = int(input("Enter high number: "))

print(" ")
print("     ***Welcome to the Great Number Guessing Game***")
print(" ")

while guessNum < guessLimit:
    try:
        guess = int(input("guess number between {} and {}:  ". format(low, high)))
        print(" ")
    except ValueError:
        print("Not at valid number. Try again")
        continue
    if guess > high or guess < low:
        print("Your guess is out of range. Please pick a number betwee {} and {}".format(low,high))
        print(" ")
    else:
        guessNum = guessNum + 1
        if guess > num:
            print("too high")
        if guess < num:
            print("too low")
        print("You have {} guesses left".format(guessNum))
        print(" ")
        pass

while True:
    var = print("Would you like to play again? (y/n):  ")
    if var == "n" or "N":
        break
if guess == num:
    print("CONGRATS!! You guess the number! ")
    print(" ")


if guessNum == guessLimit:
    print("You have guessed too many times. Goodbye")
    print("The secret number was ** {} **".format(num))
    print(" ")
