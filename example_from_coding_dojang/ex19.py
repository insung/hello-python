# 9일때
# 0: ____*        4칸 띄우고 * 1개
# 1: ___***       3칸 띄우고 * 3개
# 2: __*****      2칸 띄우고 * 5개
# 3: _*******     1칸 띄우고 * 7개
# 4: *********    0칸 띄우고 * 9개
# 5: _*******     1칸 띄우고 * 7개
# 6: __*****      2칸 띄우고 * 5개
# 7: ___***
# 8: ____*

n = int(input())
if n%2 != 1:
    print('hey!')
    exit()

star_cnt = 1
space_cnt = int(n / 2)
half = False

for a in range(n):

    if space_cnt == 0:
        half = True
        
    #print(space_cnt, star_cnt, half, end='')

    for i in range(space_cnt):
        print(' ', end='')

    for j in range(star_cnt):
        print('*', end='')

    if half:
        space_cnt += 1
        star_cnt -= 2
    else:
        space_cnt -= 1    
        star_cnt += 2
        

    print()


# 6일때        
# 0 : _____*      5칸 띄우고 * 1개
# 1 : ____***     4칸 띄우고 * 3개
# 2 : ___*****    3칸 띄우고 * 5개
# 3 : __*******   2칸 띄우고 * 7개
# 4 : _*********  1칸 띄우고 * 9개
# 5 : *********** 0칸 띄우고 * 11개

# n = int(input())
# star_cnt = 1
# space_cnt = n - 1
#
# for i in range(n):
#     for p in range(space_cnt):
#         print(' ', end='')
#     for j in range(star_cnt):
#         print('*', end='')
#
#     star_cnt += 2
#     space_cnt -= 1
#     print()
