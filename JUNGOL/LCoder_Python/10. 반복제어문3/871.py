ipt = int(input())

# *1개부터 *n개까지 구현
for i in range(1, ipt+1):
    print('*'*i)

#다시 *n-1개부터 *1개까지 구현
for j in range(ipt-1, 0, -1):
    print('*'*j)