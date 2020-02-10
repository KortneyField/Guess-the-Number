import random

for x in range(1):
  num = random.randint(1,10)

while True:
    guess = input("guess number:"  )
    if guess == num:
        print("Congradulations. You guess the number! ")
        playAgain = raw_input('Do you want to contine y/n')
        if playAgain == "n":
            break
else:
    print("Sorry not it, try again")
    pass
