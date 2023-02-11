array = []

for i in range(5):
    list = [0] * 5
    for j in range(5):
        if j % 2 == 1:
            list[j] = 1
    for k in range(1, 4):
        list[k] = list[k] + list[k+1]
        array.append(list)

print(array)
