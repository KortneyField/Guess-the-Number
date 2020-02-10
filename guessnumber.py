import random

for x in range(1):
  num = random.randint(1,10)

while True:
    guess = input("guess number:"  )
    if guess == num:
        print("congradulations")
    else:
        print("sorry not it")
        pass
