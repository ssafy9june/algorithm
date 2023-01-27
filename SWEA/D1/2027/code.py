# import sys;
# sys.stdin = open('input.txt', 'r')

for i in range(0,5):
    for j in range(0,5):
        if i == j:
            print('#', end="")
        else:
            print('+', end="")
    print('')