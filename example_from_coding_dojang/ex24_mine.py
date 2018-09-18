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

# * . * ==> 1 0 1 ==> * 4 * ==> row[0][0], {{me}}, row[0][2] // row[1][0], row[1][1], row[1][2]
# * . * ==> 1 0 1 ==> * 6 * ==> row[0][0], row[0][1], row[0][2] // row[1][0], {{me}}, row[1][2] // row[2][0], row[2][1], row[2][2]
# . * * ==> 0 1 1 ==> 2 * * ==> row[1][0], row[1][1] // {{me}}, row[2][1]

# step1.
#   me[x][y-1],   me[x][y], me[x][y+1]
# me[x+1][y-1], me[x+1][y], me[x+1][y+1]

# step2.
# me[x-1][y-1], me[x-1][y], me[x-1][y+1]
#   me[x][y-1],   me[x=1][y=1], me[x][y+]
# me[x+1][y-1], me[x+1][y], me[x+1][y+1]

# step3.
# me[x-1][y], me[x-1][y+1]
#   me[x=2][y=0], me[x][y+1]

# x_range1 = x-1, x, x+1
# x_range2 = x-1, x, x+1
# x_range3 = x, x+1

# if (x!=0


# matrix[x][y] 라고 칭함

x = 0

print('print result')
for i in matrix:
    y = 0
    for j in i:
        
        if j == 1:
            #print('* [%d][%d]' % (x, y), end=' ')
            print('*', end=' ')
        else:

            ret = 0
            
            #print('.[%d][%d]' % (x, y), end=' ')
            x_start, y_start, x_end, y_end = x, y, x, y

            # x좌표가 row-1 또는 0 일때는 2 row 만 검색, 그 외 3 row            
            #if (x==row-1) or (x==0):
            #    x_range = 2
            #    x_start = x
            #else:
            #    x_range = 3
            #    x_start = x - 1

            # y좌표가 col-1 또는 0 일때는 2칸만 검색, 그 외 3칸
            #if (y==col-1) or (y==0):
            #    y_range = 2
            #    y_start = y
            #else:
            #    y_range = 3
            #    y_start = y - 1

            #print('[%d][%d]' % (x, y), end='')
            #if (x == x_start) and (y == y_start):
            #    continue
            #else:
            #for ii in range(x_start, x_range - x_start):
            #    for jj in range(y_start, y_range - y_start):
                    #print('[%d][%d], ' % (ii, jj), end='')
                            #if matrix[ii][jj] == 1:
                            #    ret += 1
                            
            #print(x_start, x_range - x_start, end=', ')

##            step 1
##            matrix[x-1][y-1]
##            matrix[x-1][y]
##            matrix[x-1][y+1]
##
##            ==> if x-1 < 0 then skip
##            ==> if y-1 < 0 then skip
##
##            step 2
##            matrix[x][y-1]
##            matrix[x][y]   ==> skip
##            matrix[x][y+1]
##
##            step 3
##            matrix[x+1][y-1]
##            matrix[x+1]y]
##            matrix[x+1][y+1]
##
##            ==> if x+1 > len(matrix)-1 then skip
##            ==> if y+1 > len(i)-1 then skip

            #print('[', end='')
            if x-1 >= 0:
                if y-1 >= 0:
                    #print(x-1, y-1, end=',')
                    ret += matrix[x-1][y-1]
                #print(x-1, y, end=',')
                ret += matrix[x-1][y]
                if y+1 < len(i):
                    #print(x-1, y+1, end=',')
                    ret += matrix[x-1][y+1]
            #print('][', end='')

            if y-1 >= 0:
                #print(x, y-1, end=',')
                ret += matrix[x][y-1]
            #print(x, y, end=',')
            #ret += matrix[x][y]
            if y+1 < len(i):
                #print(x, y+1, end=',')
                ret += matrix[x][y+1]

            #print('][', end='')
            if x+1 < len(matrix):
                if y-1 >= 0:                    
                    #print(x+1, y-1, end=',')
                    ret += matrix[x+1][y-1]
                #print(x+1, y, end=',')
                ret += matrix[x+1][y]
                if y+1 < len(i):
                    #print(x+1, y+1, end=',')
                    ret += matrix[x+1][y+1]
            #print(']', end='')
            print(ret, end=', ')            
            
        y += 1

    #print('len: %d, %d,' % (len(matrix)-1, len(i)), end='')
        
    print()
    x += 1
