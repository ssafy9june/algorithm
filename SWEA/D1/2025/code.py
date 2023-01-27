import sys;
sys.stdin = open('input.txt', 'r')

sum = 0
for i in range(1, int(input())+1):
    sum = sum + i
print(sum)