

ipt_list = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]

total = 0

for i in range(4):
    print(*ipt_list[i])
    for j in range(3):
        total += ipt_list[i][j]

print(total)