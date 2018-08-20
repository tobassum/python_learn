import sys

n = int(input().strip())
arr = list(map(int, input().rstrip().split(" ")))

a = arr[::-1]
print(" ".join(str(x)for x in a))