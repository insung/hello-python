import random

#col, row = 3, 3

col, row = map(int, input().split())
print('enter col, row: ', col, row)


matrix = [[random.randint(0,1) for i in range(col)] for j in range(row)]

print('print value of matrix')
for i in matrix:
    for j in i:
        if j == 1:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

x = 0

print('print result')
for i in matrix:
    y = 0
    for j in i:
        
        if j == 1:
            print('*', end=' ')
        else:

            ret, x_start, x_end, y_start, y_end = 0, x-1, x+1, y-1, y+1
            
            if x-1 < 0:
                x_start = x
            if x+1 >= len(matrix):
                x_end = x

            if y-1 < 0:
                y_start = y
            if y+1 >= len(i):
                y_end = y

            for ii in range(x_start, x_end + 1):
                for jj in range(y_start, y_end + 1):
                    ret += matrix[ii][jj]
                    
            print(ret, end=', ')
        y += 1
        
    print()
    x += 1
