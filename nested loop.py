# nested loop
i = 2
while(i < 100):
    j = 2
    while(i <= (i / j)):
        if not (i % j):
            break
        j = j + 1
    if (j > (i / j)):
        print(i, "this is prime number: ")
        i = i + 1
print("Good Bye !!!!")