import sys;
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())
if a == 1 and b == 3:
    print('A')
elif a > b:
    print('A')
else:
    print('B')