import sys;
sys.stdin = open('input.txt', 'r')

num = list(map(int, input().split()))
print(num[0] - num[1] + 1)