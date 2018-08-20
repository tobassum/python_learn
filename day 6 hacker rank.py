t = int(input())

for _ in range(t):
    line = input()
    first = ""
    second = ""
    for (i, l) in enumerate(line):
        if (i & 1) == 0:
            first += l
        else:
            second += l
    print(first, second)