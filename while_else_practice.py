#guess the number and while else loop practice
#Three time user insert the number for guess


from random import randint


random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(input("Your Guess!"))
    if random_number == guess:
        print("You Win!")
        break
    guesses_left -= 1
else:
    print("You Lose")
