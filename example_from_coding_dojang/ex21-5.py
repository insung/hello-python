import turtle as t

n, line = map(int, input().split())

t.shape('turtle')
t.speed('fastest')

if (n > 10) and (n < 5):
    print('(n > 10) and (n < 5)')
    exit()

if (line > 150) and (line < 50):
    print('(line > 150) and (line < 50)')
    exit()

for i in range(n):
    t.forward(line)
    t.right((360/n) * 2)
    t.forward(line)
    t.left(360/n)
