"""Welcome to the Guessing Game and you 
   guess the number bitween 1 to 100"""

def main():
    str1 = input("Welcome to the game,Enter your Name ===>>  ")
    user_inter = False   
    while not user_inter:
        n = int(input("Enter the guess number --> " + '' + str1 + ' --->> '))
        if n == 23:
            print("You Got it, " + str1 + "  Congratulations!!!!")
            user_inter = True
        elif n < 23:
            print("You must be some higher")
        else:
            print("You must be lower")


if __name__ == "__main__":
    main()