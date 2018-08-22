from random import randint


random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    print(random_number)
    if random_number == 0:
        print("You Win!")
        break
    guesses_left += -1
else:
    print("You Lose")
