upper = int(input("enter the number: "))
lower = int(input("enter the number: "))

print("the prime number bitween", upper, "and", lower, "are: ")
for num in range(lower, upper + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
        else:
            print("%d is a prime number \n" % num)
