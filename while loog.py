#var = 1
# for infinite loop constructs
#while var == 1:
    #num = input("enter your number: ")
    #print("you entered the number is: ", num)
#print("good bye")

#Else statement in whileloop

count = 0
while count < int(input("enter the number")):
    print(count, " is less then 5")
    count += 1
else:
    print(count, " is not less then 5")