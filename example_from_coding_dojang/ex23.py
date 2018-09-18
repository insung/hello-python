import math

a, b = map(int, input().split())

if (a < 1 or a > 20) or (b < 10 or b > 30) or (a > b):
    print('error')
    exit()

r = list()

for i in range(a, b+1):
    r.append(int(math.pow(2, i)))

r.remove(r[1])
r.remove(r[len(r) - 2])

print(r)
